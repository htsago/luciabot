FROM python:3.13-slim

LABEL authors="htsago"

WORKDIR /app
RUN apt update && apt install -y build-essential
RUN pip install numpy==1.26.4
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT ["python", "lucia.py"]
