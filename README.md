# Lucia: Ein interaktiver KI-basierter Sprachdienst

Lucia ist ein Flask-basiertes Projekt, das Nutzern ermöglicht, mit einer KI zu interagieren, die Fragen beantwortet, Texte analysiert und Antworten in Audioform bereitstellt. Dieses System kombiniert Text- und Spracherkennung mit generativer KI und Text-to-Speech (TTS)-Technologie, um eine immersive Benutzererfahrung zu schaffen.

## Funktionsweise
Lucia bietet folgende Funktionen:
1. **Audioverarbeitung**: Hochgeladene Audiodateien werden transkribiert.
2. **Textverarbeitung**: Die transkribierten Inhalte werden analysiert und beantwortet.
3. **Sprachausgabe**: Die Antwort wird synthetisiert und als Audio zurückgegeben.

---

## Technologie-Stack

- **[Flask](https://flask.palletsprojects.com/)**: Für die API-Erstellung und das Servieren von Dateien.
- **[Flask-CORS](https://flask-cors.readthedocs.io/)**: Ermöglicht Cross-Origin Resource Sharing.
- **[LangChain](https://www.langchain.com/)**: Ermöglicht die Nutzung von LLMs (Large Language Models) wie OpenAI.
- **[OpenAI API](https://platform.openai.com/docs/)**: Für Textgenerierung und Sprachtranskription.
- **[Microsoft Edge TTS](https://github.com/replicate/edge-tts)**: Text-to-Speech-Synthese.
- **[asyncio](https://docs.python.org/3/library/asyncio.html)**: Für asynchrone Verarbeitung.
- **[base64](https://docs.python.org/3/library/base64.html)**: Kodierung der Audiodateien in Base64-Format.

---

## Installation

### 1. Klone das Repository
```bash
git clone git@github.com:htsago/luciabot.git
cd luciabot
```

### 2. Erstelle eine virtuelle Umgebung
```bash
python3 -m venv venv
source venv/bin/activate  # Für Linux/Mac
venv\Scripts\activate     # Für Windows
```

### 3. Installiere die Abhängigkeiten
```bash
pip install -r requirements.txt
```

---

## Konfiguration

1. **API-Key für OpenAI**: 
   - Speichere deinen API-Key in der Umgebungsvariable `OPENAI_API_KEY`. 
   - Füge folgende Zeile zu `~/.bashrc` oder `~/.zshrc` hinzu (Linux/Mac):
     ```bash
     export OPENAI_API_KEY="DEIN_API_KEY"
     ```
     Lade die Änderungen:
     ```bash
     source ~/.bashrc
     ```
   - Für Windows:
     ```cmd
     set OPENAI_API_KEY=DEIN_API_KEY
     ```

2. **Index-HTML-Datei**: Stelle sicher, dass sich eine `index.html` im Verzeichnis `templates/` befindet.

---

## Nutzung

### Starte den Server
```bash
python app.py
```
### **Alternativ: Mit Docker**

```bash
# Docker-Image bauen:
docker build -t luciabot .

# Container ausführen:
docker run -d -p 5000:5000 --name luciabot_container -e OPENAI_API_KEY="set your api key here" luciabot

# Container stoppen und löschen:
docker rm -f luciabot_container

# Logs einsehen:
docker logs luciabot_container
=======
#### Docker-Image bauen:
```bash
docker build -t luciabot .
```
### Container ausführen:

```bash
docker run -d -p 5000:5000 --name luciabot_container -e OPENAI_API_KEY="set your api key here" luciabot
```

### Container stoppen und löschen:

```bash
docker rm -f luciabot_container
```
### Logs einsehen:
```bash
docker logs luciabot_container
```

### Endpunkte

#### 1. **`/`**: Liefert die `index.html`-Datei aus.
- **Methode**: `GET`
- **Rückgabe**: Statische HTML-Seite.

#### 2. **`/process_audio`**: Verarbeitet eine Audiodatei.
- **Methode**: `POST`
- **Daten**: `audio_data` (Hochgeladene Datei)
- **Antwort**:
  - `user_text`: Transkribierter Text.
  - `assistant_text`: Antwort der KI.
  - `audio`: Base64-kodierte Audioantwort.

---

## Code-Übersicht

### Hauptkomponenten
1. **PromptTemplate**: Konfiguriert den Interaktionsstil von Lucia.
2. **LLMChain**: Implementiert die Logik zur Verarbeitung von Nutzeranfragen.
3. **Synthesize Speech**: Generiert eine Audioausgabe basierend auf Text.

### Beispiel-Prompt:
```plaintext
Dein Dienstname ist "Lucia" und du beantwortest die Fragen von Nutzern in einem Ton und Akzent.
{history}
Human: {human_input}
Assistant:
```

---

## Abhängigkeiten

Eine vollständige Liste der Bibliotheken findest du in der Datei `requirements.txt`. Wichtigste Abhängigkeiten sind:
- `Flask`
- `Flask-CORS`
- `openai`
- `langchain-community`
- `langchain-core`
- `edge-tts`

---

## Fehlerbehandlung

Falls ein Fehler auftritt, gibt die API:
- **HTTP 400**: Bei ungültigen Anfragen (z. B. fehlende Audiodateien).
- **HTTP 500**: Bei internen Verarbeitungsfehlern.

---

## Ressourcen

- **Flask Dokumentation**: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- **OpenAI API**: [https://platform.openai.com/docs/](https://platform.openai.com/docs/)
- **Edge TTS**: [https://github.com/replicate/edge-tts](https://github.com/replicate/edge-tts)
- **LangChain**: [https://www.langchain.com/](https://www.langchain.com/)

