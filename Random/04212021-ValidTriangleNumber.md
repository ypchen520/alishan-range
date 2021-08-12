# Valid Triangle Number

## Description

* Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

## Solution

### Brute Force

* TLE

### Binary Search

* Sort once
* the inequalities **c + a > b** and **c + b > a** are satisfied implicitly by virtue of the property **a < b < c**
* find right limit value k for each pair (i,j)
