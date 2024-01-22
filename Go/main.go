package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"time"

	_ "github.com/lib/pq"
)

var db *sql.DB

const dateFmt string = "02-01-2006 15:04:05"
const pyRequest string = "http://service_py:80/greet?name=Go"

type Log struct {
	Date string `json:"date"`
}

func main() {
	initDB()
	mux := http.NewServeMux()

	mux.HandleFunc("/greet", greetHandler)
	mux.HandleFunc("/greet/history", historyHandler)
	mux.HandleFunc("/greet/python", pythonHandler)

	s := &http.Server{
		Addr:    ":8081",
		Handler: mux,
	}
	s.ListenAndServe()
}

func initDB() {
	var err error
	connStr := "postgres://postgres:wertyxar665@db_postgres/postgres?sslmode=disable" // OKn`t
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
	fmt.Println("Table history_go created")
	_, err = db.Exec("CREATE TABLE IF NOT EXISTS public.go_requests(request VARCHAR(50), answer VARCHAR(50), date character varying NOT NULL)")
	if err != nil {
		panic(err)
	}
	fmt.Println("Table go_requests created")
}

func db_add_history() {
	_, err := db.Exec("INSERT INTO history_go (date) VALUES ($1)", time.Now().Format(dateFmt))
	if err != nil {
		panic(err)
	}
	db.Exec("COMMIT")
}

func db_add_request(request, answer string) {
	_, err := db.Exec("INSERT INTO go_requests (request, answer, date) VALUES ($1, $2, $3)", request, answer, time.Now().Format(dateFmt))
	if err != nil {
		panic(err)
	}
	db.Exec("COMMIT")
}

func db_get_history() []byte {
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
	db_add_history()
}

func historyHandler(res http.ResponseWriter, req *http.Request) {
	data := db_get_history()
	res.WriteHeader(200)
	res.Write(data)
}

func pythonHandler(res http.ResponseWriter, req *http.Request) {
	data := get_greet_py()
	res.WriteHeader(200)
	res.Write(data)
	db_add_request(pyRequest, string(data))
}

func get_greet_py() []byte {
	resp, err := http.Get(pyRequest)
	if err != nil {
		return []byte("Python сервис не отвечает")
	}
	body, _ := io.ReadAll(resp.Body)
	return body
}
