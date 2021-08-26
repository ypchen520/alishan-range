# Sum of Square Numbers

## Description

* Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

## Solution

### Binary Search

*  find an integer, mid, in the range [0, c - a^2], such that mid×mid=c−a^2
