# Russian Doll Envelopes

## Description

* You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
* One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.
* Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
* Note: You cannot rotate an envelope.

## Solution

### [Longest Increasing Subsequence](https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/)

* First sort the width w in ascending order. If you encounter the situation where w is the same, sort by height h in descending order.
* Find the length of LIS on h
