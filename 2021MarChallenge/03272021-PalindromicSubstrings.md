# Palindromic Substrings

## Description

* Given a string, your task is to count how many palindromic substrings in this string.
* The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

## Solution

### Hint

* How can we reuse a previously computed palindrome to compute a larger palindrome?
* If “aba” is a palindrome, is “xabax” and palindrome? Similarly is “xabay” a palindrome?
* Complexity based hint:
  * If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n<sup>2</sup>) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation?

### [DP](https://www.geeksforgeeks.org/count-palindrome-sub-strings-string/)

#### Top-down (memoization)

* Base condition: i > j
* Check for each and every i and j, if the characters are equal
* Call the is_palindrome function again with incremented i  and decremented j
* Check this for all values of i and j by applying 2 for loops