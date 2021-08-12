# Longest Word in Dictionary through Deleting

## Description

* Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

## Solution

### Time Complexity O(nw)

* **isSubsequence**: Use separate function to see if the letter can be found after its previous character

   ```python
   def is_subseq(self, word, s):
      if len(word) > len(s): 
            return False
      pos = 0
      for c in word:
         pos = s.find(c, pos)
         if pos == -1:
            return False
         pos += 1
      return True
   ```
