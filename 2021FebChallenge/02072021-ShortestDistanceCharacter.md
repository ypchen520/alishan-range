# Shortest Distance to a Character

## Description

* Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.

## Solution

### Traverse twice

* When going from left to right, we'll remember the index **prev** of the last character c we've seen.
  * the answer is **i - prev**
* When going from right to left, we'll remember the index **prev** of the last character c we've seen.
  * the answer is prev - i.
* We take the minimum of these two answers to create our final answer.
