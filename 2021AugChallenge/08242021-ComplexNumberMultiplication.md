# Complex Number Multiplication

## Description

* A complex number can be represented as a string on the form "real+imaginaryi" where:
  * real is the real part and is an integer in the range [-100, 100].
  * imaginary is the imaginary part and is an integer in the range [-100, 100].
  * i<sup>2</sup> == -1.
* Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

## Solution

### Java

* str.split()
  * + is a reserved character in regexes, so you need to escape it
    
    ```java
    String [] splitted = str.split("\\+");
    ```
* [remove trailing characters](https://www.baeldung.com/java-remove-trailing-characters)
  * subString()
* convert String to int: Integer.parseInt()
* convert String into Integer: Integer.valueOf()
* convert int to String: String.valueOf() or Integer.toString()
