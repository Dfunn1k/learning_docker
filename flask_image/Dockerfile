FROM python:3.10-alpine3.18

# Path: /app

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]