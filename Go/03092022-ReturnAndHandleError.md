# Return and handle an error

* Any Go function can return multiple values.
  * One of Go's unusual features is that functions and methods can return multiple values.

  ```Go
  return x, i
  ```
* Add nil (meaning no error) as a second value in the successful return. That way, the caller can see that the function succeeded.