FROM python:3.9-slim


WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000

# On lance main.py qui est dans le dossier api
CMD ["python", "api/main.py"]