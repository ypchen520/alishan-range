# Tutorial: Create a Go module

* Create a module -- Write a small module with functions you can call from another module.
* Call your code from another module -- Import and use your new module.
* Return and handle an error -- Add simple error handling.
* Return a random greeting -- Handle data in slices (Go's dynamically-sized arrays).
* Return greetings for multiple people -- Store key/value pairs in a map.
* Add a test -- Use Go's built-in unit testing features to test your code.
* Compile and install the application -- Compile and install your code locally.

## Start a module that others can use

* In a module, you collect one or more related packages for a discrete and useful set of functions
* Go code is grouped into packages, and packages are grouped into modules
* If you publish a module, this must be a path from which your module can be downloaded by Go tools. That would be your code's repository
  * example.com/greetings

## Call your code from another module

* In Go, code executed as an application must be in a main package
* because you haven't published the module yet, you need to adapt the example.com/hey module so it can find the example.com/greetings code on your local file system
* run the go mod tidy command to synchronize the example.com/hey module's dependencies, adding those required by the code, but not yet tracked in the module

## Resources

* [how-to-use-go-modules](https://www.digitalocean.com/community/tutorials/how-to-use-go-modules)