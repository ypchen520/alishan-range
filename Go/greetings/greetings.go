package greetings

import (
	"errors"
	"fmt"
)

func Hello(name string) string {
	// var message sting
	// message = fmt.Sprintf("Hi, %v. Welcome", name)
	message := fmt.Sprintf("Hi, %v. Welcome!", name)
	return message
}