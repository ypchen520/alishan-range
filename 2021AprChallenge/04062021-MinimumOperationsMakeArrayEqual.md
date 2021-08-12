# Minimum Operations to Make Array Equal

## Description

* You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).
* In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.
* Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.

## Solution

### Hint

* Build the array arr using the given formula, define target = sum(arr) / n
* What is the number of operations needed to convert arr so that all elements equal target?

### Math

* target = sum(arr)/n = n<sup>2</sup>/n = n
* sum of n consecutive even integers = n(n+1)
* sum of n consecutive odd integers = n<sup>2</sup>
