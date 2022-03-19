package greetings

import (
	"errors"
	"fmt"
)

func Hello(name string) (string, error) {
	// var message sting
	// message = fmt.Sprintf("Hi, %v. Welcome", name)
	if name == "" {
		return "", errors.New("empty name")
	}
	message := fmt.Sprintf("Hi, %v. Welcome!", name)
	return message, nil
}