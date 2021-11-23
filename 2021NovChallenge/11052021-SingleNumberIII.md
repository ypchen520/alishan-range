# Single Number III

## Description

* Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
* You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

## Solution

### Bit Manipulation using XOR

* x ^ x = 0
* two's complement
  * invert all bits then add one
  * 0101 -> 1010 + 1 = 1011
  * x & -x = 0101 & 1011 = 0001 (the right most set bit)
* First pass
  * xor everything to get y = A^B
  * find the rightmost different bit of A and B by calculating z = y & -y
* Second pass
  * see if num & z != 0: numbers that include A or B
    * xor these numbers to get A or B
* y ^ A = B (y ^ B = A)
