FROM python:3.9-slim

ENV PGHOST city_database
ENV PGPORT 5432
ENV PGUSER postgres
ENV PGPASSWORD postgres_pw

WORKDIR /app
COPY function /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1337

CMD ["python", "app.py"]
