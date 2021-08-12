# Concatenation of Consecutive Binary Numbers

## Description

* Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7

## Solution

### Hint

* Express the nth number value in a recursion formula and think about how we can do a fast evaluation.

### Python

* int to binary string
  * get_bin = lambda x: format(x, 'b')
* binary string to int
  * int('11111111', 2)
* Bitwise operators
  * <<, >>, &, |, ~, ^

### Bit Operation

### Modulo

* modulo is distributive over +, * and – but not over /
  * (a + b) % c = ( ( a % c ) + ( b % c ) ) % c
  * (a * b) % c = ( ( a % c ) * ( b % c ) ) % c
  * (a – b) % c = ( ( a % c ) – ( b % c ) ) % c
  * [(a + b) * c] % z = {[(a + b) % z] * c} % z
