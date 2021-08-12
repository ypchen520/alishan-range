# A Tour of Go

## Packages

* Every Go program is made up of packages
* Programs start running in package main.

```Go
package main
func main() {
}
```

* using the packages with import paths

```Go
import (
    "fmt"
    "math/rand"
)
```

## Imports

This code groups the imports into a parenthesized, "factored" import statement.

## Exported names

* In Go, a name is exported if it begins with a capital letter.
* When importing a package, you can refer only to its exported names. Any "unexported" names are not accessible from outside the package.

## Functions

* A function can take **zero** or more arguments.
* Notice that the type comes after the variable name.
* When two or more consecutive named function parameters share a type, you can omit the type from all but the last.
  * ```x int, y int``` to ```x, y int```

```Go
func add(x int, y int) int {
    return x + y
}
```

### Multiple results

* A function can return any number of results.

### Named return values

* Go's return values may be named. If so, they are treated as variables defined at the top of the function.
* A return statement without arguments returns the named return values. This is known as a "naked" return.
* Naked return statements should be used only in **short functions**, as with the example shown here. They can harm readability in longer functions.

```Go
package main

import "fmt"

func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}

func main() {
    fmt.Println(split(17))
}
```

## Variables

* The var statement declares a list of variables; as in function argument lists, the type is last.
* A var statement can be at package or function level. We see both in this example.

### Variables with initializers

* A var declaration can include initializers, one per variable.
* If an initializer is present, the type can be omitted; the variable will take the type of the initializer.

```Go
package main

import "fmt"

var i, j int = 1, 2

func main() {
    var c, python, java = true, false, "no!"
    fmt.Println(i, j, c, python, java)
}
```

### Short variable declarations

* Inside a function, the := short assignment statement can be used in place of a var declaration with implicit type.
* Outside a function, every statement begins with a keyword (var, func, and so on) and so the := construct is not available.

### Basic types

* variable declarations may be "factored" into blocks, as with import statements.

```Go
package main

import (
    "fmt"
    "math/cmplx"
)

var (
    ToBe   bool       = false
    MaxInt uint64     = 1<<64 - 1
    z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func main() {
    fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
    fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
    fmt.Printf("Type: %T Value: %v\n", z, z)
}
```

### Zero values

* Variables declared without an explicit initial value are given their zero value.
  * 0 for numeric types
  * false for the boolean type, and
  * "" (the empty string) for strings

```Go
package main

import "fmt"

func main() {
    var i int
    var f float64
    var b bool
    var s string
    fmt.Printf("%v %v %v %q\n", i, f, b, s)
}
```

### Type conversions

* The expression T(v) converts the value v to the type T.

### Type inference

* When declaring a variable without specifying an explicit type (either by using the := syntax or var = expression syntax), the variable's type is inferred from the value on the right hand side.
* But when the right hand side contains an untyped numeric constant, the new variable may be an int, float64, or complex128 depending on the precision of the constant

### Constants

* Constants are declared like variables, but with the const keyword.
* Constants cannot be declared using the := syntax.

### Numeric Constants

* Numeric constants are high-precision values.
* An untyped constant takes the type needed by its context.

## For

* Go has only one looping construct, the for loop.
