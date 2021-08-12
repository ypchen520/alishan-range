# Remove All Adjacent Duplicates In String

## Description

* You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
  * We repeatedly make duplicate removals on s until we no longer can.
* Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

## Solution

### Hint

* Use a stack to process everything greedily

### Java

* Stack
  * pop()
  * peek()
  * push()
  * empty()
* String
  * length()
  * toCharArray()
  * charAt
* Character (char)
