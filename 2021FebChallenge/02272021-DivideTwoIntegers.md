# Divide Two Integers

## Description

* Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

* Return the quotient after dividing dividend by divisor.

* The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

* Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

## Solution

### O(logn)

* since we cannot use multiplication, we are using left shifting
