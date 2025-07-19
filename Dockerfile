FROM python:3.10-slim

RUN apt-get update && apt-get install -y default-jre wget unzip

# Installer signal-cli
RUN wget https://github.com/AsamK/signal-cli/releases/download/v0.11.1/signal-cli-0.11.1-Linux.tar.gz \
    && tar -xzf signal-cli-0.11.1-Linux.tar.gz \
    && mv signal-cli-0.11.1 /app/signal-cli \
    && rm signal-cli-0.11.1-Linux.tar.gz

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
