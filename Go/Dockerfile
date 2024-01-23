FROM golang:1.21.3

#параметры postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD 123456
ENV POSTGRES_HOST db_postgres
ENV POSTGRES_PORT 5432
ENV POSTGRES_DBNAME postgres

RUN mkdir /src
ADD . ./src
WORKDIR ./src
RUN go get .
RUN go build -o main
CMD ["./main"]