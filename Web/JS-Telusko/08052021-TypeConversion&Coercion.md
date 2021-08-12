# Type Conversion & Coercion

## Type Conversion: explicit conversion

* Number()
* String()
* Boolean(0): false
  * other numbers: true
* Boolean(null): false
* Boolean(undefined): false
* **parseInt**
  * parseInt("123 Yu-Peng")

## Type Coercion

```JavaScript
let x
console.log(x, typeof x)
x = 8
console.log(x, typeof x)
x = x + ''
console.log(x, typeof x)
x = x - 2
console.log(x, typeof x)
```
