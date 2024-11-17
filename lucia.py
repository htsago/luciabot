from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
import edge_tts
import asyncio
from io import BytesIO
import openai
import base64
import os

app = Flask(__name__)
CORS(app)

TEMPLATE_TEXT = """Dein Dienstname ist "Lucia" und du beantwortest die Fragen von Nutzern in einem Ton und Akzent.
{history}
Human: {human_input}
Assistant:"""

openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = PromptTemplate(input_variables=["history", "human_input"], template=TEMPLATE_TEXT)
chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0),
    prompt=prompt,
    verbose=True,
    memory=ConversationBufferWindowMemory(k=3)
)

async def synthesize_speech(text):
    """
    Synthetisiert Text in Audio mit Microsoft Edge TTS und gibt ein Audio-Stream zurück.
    """
    voice = 'de-DE-KatjaNeural'
    communicate = edge_tts.Communicate(text=text, voice=voice)
    audio_output = BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_output.write(chunk["data"])
    audio_output.seek(0)
    return audio_output


@app.route('/')
def serve_index():
    return send_file('templates/index.html')


@app.route('/process_audio', methods=['POST'])
def process_audio():
    """
    Verarbeitet eine hochgeladene Audiodatei:
    1. Transkribiert das Audio.
    2. Generiert eine Antwort.
    3. Synthetisiert die Antwort in Audio und sendet die Antwort als JSON zurück.
    """
    if 'audio_data' not in request.files:
        return jsonify({'error': 'Keine Audiodaten bereitgestellt'}), 400

    audio_file = request.files['audio_data']
    audio_data = audio_file.read()

    try:
        audio_bytes = BytesIO(audio_data)
        audio_bytes.name = 'audio.webm'

        transcript = openai.Audio.transcribe("whisper-1", audio_bytes, language="de")
        user_text = transcript["text"]
        print(f"Erkannter Text: {user_text}")

        assistant_text = chatgpt_chain.predict(human_input=user_text)
        print(f"Antwort: {assistant_text}")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        audio_output = loop.run_until_complete(synthesize_speech(assistant_text))
        audio_base64 = base64.b64encode(audio_output.read()).decode('utf-8')

        return jsonify({
            'user_text': user_text,
            'assistant_text': assistant_text,
            'audio': audio_base64
        })

    except Exception as e:
        print(f"Fehler bei der Verarbeitung: {e}")
        return jsonify({'error': 'Fehler bei der Verarbeitung', 'details': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
