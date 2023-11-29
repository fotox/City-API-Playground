FROM python:3.11.3-slim-buster

ENV BASIC_AUTH_USERNAME admin
ENV BASIC_AUTH_PASSWORD password
ENV PGHOST postgres
ENV PGPORT 5432
ENV PGUSER postgres
ENV PGPASSWORD postgres_pw
ENV PGDATABASE city
ENV PGSCHEME prod

WORKDIR /usr/src/app
COPY function /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

EXPOSE 1337

CMD ["python", "app.py"]
