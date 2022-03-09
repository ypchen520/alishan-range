# [Tutorial: Get started with Go](https://go.dev/doc/tutorial/getting-started)

* Install Go (if you haven't already).
* Write some simple "Hello, world" code.
* Use the go command to run your code.
* Use the Go package discovery tool to find packages you can use in your own code.
* Call functions of an external module.

## Write some code

* go.mod
  * When your code imports packages contained in other modules, you manage those dependencies through your code's own module. 
  * That module is defined by a go.mod file that tracks the modules that provide those packages
  * the module path will typically be the repository location where your source code will be kept
    * github.com/mymodule
* Package
  * a package is a way to **group functions**, and it's **made up of all the files in the same directory**
  * A main function executes by default when you run the main package

## Call code in an external package

* pkg.go.dev
* Add new module requirements and sums
  * ```go mod tidy```
  * add the quote module as a requirement
  * add a go.sum file for use in authenticating the module
