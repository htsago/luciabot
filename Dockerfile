FROM python:3.13-slim

LABEL authors="htsago"


WORKDIR /app


RUN apt update && apt install -y build-essential nginx


RUN pip install numpy==1.26.4


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .
COPY nginx.conf /etc/nginx/nginx.conf


EXPOSE 5000 80

CMD ["sh", "-c", "service nginx start && gunicorn -b 0.0.0.0:5000 lucia:app"]