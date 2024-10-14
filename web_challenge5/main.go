package main

import (
	"github.com/joho/godotenv"
	"log"
	"net/http"
	"os"
)

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}
	port := os.Getenv("PORT")
	if port == "" {
		port = "8005"
	}

	// Define a simple handler for the root path
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("The API awaits your command; have you got the key?"))
	})

	// Define a handler for the /flag endpoint
	http.HandleFunc("/flag", func(w http.ResponseWriter, r *http.Request) {
		apiKey := r.Header.Get("X-API-Key")

		// Hardcoded API key for the challenge
		APIKey := "9d531987-7e49-45a7-889a-69a84fb7134e"

		if apiKey == APIKey {
			flag := os.Getenv("FLAG")
			w.Write([]byte("Here's your flag: " + flag))
		} else {
			// If the API key is incorrect, respond with an error message
			http.Error(w, "Unauthorized", http.StatusUnauthorized)
		}
	})

	log.Printf("Server started on :%s", port)

	// Start the server, listening on all interfaces
	err = http.ListenAndServe("0.0.0.0:"+port, nil)
	if err != nil {
		log.Fatalf("Server failed to start: %v", err)
	}
}
