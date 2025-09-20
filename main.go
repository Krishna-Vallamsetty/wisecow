package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Moo! Hello from the Wisecow Go Application!")
}

func main() {
	http.HandleFunc("/", handler)
	log.Println("Starting Wisecow server on port 8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

