# Longest Substring Without Repeating Characters

## Description

* Given a string s, find the length of the longest substring without repeating characters
* Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Solution

### Brute Force

* check every substring
* n*(n+1)/2 possible substrings
  * n(n-1)/2 + n
    * for example, abcde
      * n(n-1)/2
        * pair a with b, bc, bcd, bcde -> (n-1) options
        * pair b with a, ac, acd, acde -> (n-1) options
        * ...
      * n
        * a, b, ..., e
* time complexity is O(n^2)

### Linear time complexity

* We start with traversing the string from left to right and keep track of:
  * the current substring with non-repeating characters with the help of a start and end index
    * start = max(visited[s[end]] + 1, start)
      * max is used to avoid going back to elements that are already traversed
  * the longest non-repeating substring output
  * a lookup table of already visited **characters**

### Python

* substring
  * str[start:end(not included)]
* dict.has_key()
  * only Python2
