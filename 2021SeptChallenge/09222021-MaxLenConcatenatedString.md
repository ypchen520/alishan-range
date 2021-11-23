# Maximum Length of a Concatenated String with Unique Characters

## Description

* Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
* Return the maximum possible length of s.

## Solution

* iterate through the input strings
  * skip the word that have duplicate characters
* for each string
  * check if it conflicts with the combinations that are currently found

### Hint

* You can try all combinations and keep mask of characters you have.
* You can use DP.

### DP
