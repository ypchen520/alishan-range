# Add Strings

## Description

* Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
* You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

## Solution

### Java

* for loop with two variables
* StringBuilder sb = new StringBuilder();
  * sb.reverse()
  * sb.toString()
* int x = i < 0 ? 0 : num1.charAt(i) - '0';
  * convert string to integer in Java: str - '0'
