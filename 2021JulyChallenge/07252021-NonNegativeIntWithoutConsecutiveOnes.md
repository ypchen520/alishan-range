# Non-negative Integers without Consecutive Ones

## Description

* Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

## Solution

### DP

* Get the binary format of the input integer **num**
  * the binary format is **reversed**: the least significant bit (**LSB**) is at the beginning
* Find the number of integers of **length n** that have no consecutive ones in its binary format
  * n equals the length of the input integer num in its binary format (possible longest string)
  * ones[i]: Nummber of integers of **length i** that end with an one and have no consecutive ones in its binary format
    * equals zeros[i-1]
  * zeros[i]: Nummber of integers of **length i** that end with a zero and have no consecutive ones in its binary format
    * equals zeros[i-1] + ones[i-1]
* Remove the integers that are larger then num
  * For example, if num = 8
    * the length n will be 4
    * when we calculate ones[4] = zeros[3], we are actually considering adding a '1' to the right of '100', resulting in '1001', which exceeds the input num '1000'
  * This can be done by detecting consecutive zeros starting from the MSB

### Java

* StringBuilder
  * we can modified characters using a StringBuilder (we can't if we use a String)
* Integer.toBinaryString()
* reverse a string

```Java
new StringBuilder(hi).reverse().toString()
```
