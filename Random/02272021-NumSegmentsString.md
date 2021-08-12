# Number of Segments in a String

## Description

* You are given a string s, return the number of segments in the string. 
* A segment is defined to be a contiguous sequence of non-space characters.

## Solution

### Using Language Builtins

* Python: len(s.split())

### In-place

* if(i == 0 or s[i-1] == ' ') and s[i] != ' ': count += 1
