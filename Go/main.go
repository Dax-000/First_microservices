package main

import (
	"database/sql"
	"fmt"
	"net/http"
	"time"

	_ "github.com/lib/pq"
)

var db *sql.DB

type logs struct {
	name string `json:"name"`
	date string `json:"date"`
}

func main() {
	initDB()
	mux := http.NewServeMux()

	mux.HandleFunc("/greet", greetHandler)
	mux.HandleFunc("/greet/history", historyHandler)

	s := &http.Server{
		Addr:    ":8080",
		Handler: mux,
	}
	s.ListenAndServe()
}

func initDB() {
	var err error
	connStr := "postgres://postgres:wertyxar665@localhost/postgres?sslmode=disable" // OKn`t
	db, err = sql.Open("postgres", connStr)

	if err != nil {
		panic(err)
	}
	if err := db.Ping(); err != nil {
		panic(err)
	}
	fmt.Println("The database is connected")
}

func add_history() {
	_, err := db.Exec("INSERT INTO history (name, date) VALUES ($1, $2)", "noname", time.Now().Format("02-01-2006 15:04:05"))
	if err != nil {
		panic(err)
	}
	db.Exec("COMMIT")
}

func greetHandler(res http.ResponseWriter, req *http.Request) {
	data := []byte("Привет от Go!")
	res.WriteHeader(200)
	res.Write(data)
	add_history()
}

func historyHandler(res http.ResponseWriter, req *http.Request) {

	data := []byte("Здесь должна быть история")
	res.WriteHeader(200)
	res.Write(data)
}
