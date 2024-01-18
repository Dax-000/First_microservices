package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	_ "github.com/lib/pq"
)

var db *sql.DB

type Log struct {
	Date string `json:"date"`
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
	_, err = db.Exec("CREATE TABLE IF NOT EXISTS public.history_go(date character varying NOT NULL)")
	if err != nil {
		panic(err)
	}
	fmt.Println("Table history_go exists")
}

func add_history() {
	_, err := db.Exec("INSERT INTO history_go (date) VALUES ($1)", time.Now().Format("02-01-2006 15:04:05"))
	if err != nil {
		panic(err)
	}
	db.Exec("COMMIT")
}

func get_history() []byte {
	logs := make([]Log, 0)
	rows, err := db.Query("SELECT date FROM history_go")
	if err != nil {
		panic(err)
	}

	for rows.Next() {
		p := Log{}
		err := rows.Scan(&p.Date)
		if err != nil {
			fmt.Println(err)
			continue
		}
		logs = append(logs, p)
	}
	json_data, err := json.Marshal(logs)
	return json_data
}

func greetHandler(res http.ResponseWriter, req *http.Request) {
	data := []byte("Привет от Go!")
	res.WriteHeader(200)
	res.Write(data)
	add_history()
}

func historyHandler(res http.ResponseWriter, req *http.Request) {
	data := get_history()
	res.WriteHeader(200)
	res.Write(data)
}
