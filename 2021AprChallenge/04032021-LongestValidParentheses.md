# Longest Valid Parentheses

## Description

* Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

## Solution

### Brute Force

* find all substrings
* check if a substring is valid or not in linear time using a [stack](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/)

### [Stack](https://www.geeksforgeeks.org/length-of-the-longest-valid-substring/)

* O(n) time
* store indexes of previous starting brackets in a stack
* The first element of the stack is a special element that provides index before the beginning of valid substring (base for next valid string)
  * Create an empty stack and push -1 to it

#### Python

* pop()
  * The pop() method takes a single argument (index).
  * The argument passed to the method is optional. If not passed, the default index -1 is passed as an argument (index of the last item).
  