# Minimum Remove to Make Valid Parentheses

## Description

* Given a string s of '(' , ')' and lowercase English characters.
* Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
* Formally, a parentheses string is valid if and only if:
  * It is the empty string, contains only lowercase characters, or
  * It can be written as AB (A concatenated with B), where A and B are valid strings, or
  * It can be written as (A), where A is a valid string.

## Solution

### Hint

* Each prefix of a balanced parentheses has a number of open parentheses greater or equal than closed parentheses, similar idea with each suffix.
* Check the array from left to right, remove characters that do not meet the property mentioned above, same idea in backward way.
