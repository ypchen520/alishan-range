package main

import  (
	"fmt"
	"example.com/greetings"
)

func main() {
	message := greetings.Hello("Dennis")
	fmt.Println(message)
}