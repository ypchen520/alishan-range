package main

import  (
	"fmt"
	"log"
	"example.com/greetings"
)

func main() {
	log.SetPrefix("greetings: ")
	log.SetFlags(0) // a flag to disable printing the time, source file, and line number.

	message, err := greetings.Hello("")
	if err != nil {
		log.Fatal(err)
	}
    

	// message := greetings.Hello("Dennis")
	fmt.Println(message)
}