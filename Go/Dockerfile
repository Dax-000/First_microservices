FROM golang:1.21.3
RUN mkdir /src
ADD . ./src
WORKDIR ./src
RUN go get .
RUN go build -o main
CMD ["./main"]