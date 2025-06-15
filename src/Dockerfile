FROM python:3.10-slim

WORKDIR /app

# Copia apenas o requirements para usar cache de build se não mudar dependências
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código
COPY . .

EXPOSE 8080

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
