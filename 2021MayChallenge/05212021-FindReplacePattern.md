# Find and Replace Pattern

## Description

* Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
* A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
* Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

## Solution

### Two Maps

### One Map

### Python

* compare two lists and see if they are identical

```Python
if sorted(list(w_dict.values())) == sorted(list(pat_dict.values())):
```
