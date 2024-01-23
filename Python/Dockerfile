FROM python:3

#параметр app_workers uvicorn
ENV APP_WORKERS 1

#параметры postgres
ENV POSTGRES_HOST db_postgres
ENV POSTGRES_PORT 5432
ENV POSTGRES_DBNAME postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 123456

WORKDIR /src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py"]