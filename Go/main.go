package main

import (
	"net/http"
)

func main() {
	mux := http.NewServeMux()

	mux.HandleFunc("/greet", greetHandler)
	mux.HandleFunc("/greet/history", historyHandler)

	s := &http.Server{
		Addr:    ":8080",
		Handler: mux,
	}
	s.ListenAndServe()
}

func greetHandler(res http.ResponseWriter, req *http.Request) {
	data := []byte("Привет от Go!")
	res.WriteHeader(200)
	res.Write(data)
}

func historyHandler(res http.ResponseWriter, req *http.Request) {
	data := []byte("Здесь должна быть история")
	res.WriteHeader(200)
	res.Write(data)
}
