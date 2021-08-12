# Count Sorted Vowel Strings

## Description

* Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
* A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

## Solution

### Hint

* For each character, its possible values will depend on the value of its previous character, because it needs to be not smaller than it.
* Think backtracking. Build a **recursive function count(n, last_character)** that counts the number of valid strings of length n and whose first characters are not less than last_character.
* In this recursive function, iterate on the possible characters for the first character, which will be all the vowels not less than last_character, and **for each possible value c, increase the answer by count(n-1, c)**.

### Time Limit Exceed (TLE)

* start with length n
  * for 'a', we have 5 vowels to construct the strings with length = n-1
    * for j in range(0, 5):
      * for 'a', we have 5 vowels to construct the strings with length = n-2
      * for 'e', we have 4 vowels to construct the strings with length = n-2
      * and so on
  * for 'e', we have 4 vowels to construct the strings with length = n-1
    * for j in range(1, 5):
  * and so on
* call the function recursively
* base case:
  * **if n == 0: return 1**

### Top-down approach, Memoization

### Bottom-up approach

### Bottom-up approach, memory optimization
