# Longest Palindromic Substring

## Description

* Given a string s, return the longest palindromic substring in s

## Solution

### Hint

* How can we reuse a previously computed palindrome to compute a larger palindrome?
* If “aba” is a palindrome, is “xabax” and palindrome? Similarly is “xabay” a palindrome?
* Complexity based hint:
If we use brute-force and check whether for every start and end position a substring is a palindrome we have O(n^2) start - end pairs and O(n) palindromic checks. Can we reduce the time for palindromic checks to O(1) by reusing some previous computation.

### Brute force

* O(n^3)

### DP

* storing results of sub-problems
* Maintain a boolean table[n][n] that is filled in **bottom up** manner
* To calculate table[i][j], check the value of table[i+1][j-1], if the value is true and str[i] is same as str[j], then we make table[i][j] true.
* We have to fill table previously for substring of length = 1 and length = 2
* Time complexity: O(n^2)
* Space complexity: O(n^2)

### Generate all even length and odd length palindromes

* The idea is to generate all even length and odd length palindromes and keep track of the longest palindrome seen so far
* To generate odd length palindrome, fix a center and **expand in both directions** for longer palindromes, i.e. fix i (index) as center and two indices as i1 = i+1 and i2 = i-1
* even length
  * Take two indices i1 = i and i2 = i-1.
* Time complexity: O(n^2)
* **Space complexity: O(1)**

### Python

* substrings
  * s = s[beginning : beginning + LENGTH]
* three conditions
  * or: while any([CON1, CON2, CON3])
  * and: while all([CON1, CON2, CON3])
