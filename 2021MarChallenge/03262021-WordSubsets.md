# Word Subsets

## Description

* We are given two arrays A and B of words.  Each word is a string of lowercase letters.
* Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".
* Now say a word a from A is universal if for every b in B, b is a subset of a.
* Return a list of all universal words in A.  You can return the words in any order.

## Solution

* [Solution](https://www.cnblogs.com/grandyang/p/11623684.html)
  * Because now all the words set B must be a subset of A in a word, in fact, so long as for each letter, all the statistics of the maximum number of set B in a word appearing, such as for example, B = [ "eo", "oo"], wherein at most 1 occurrence e, and o occurs up to 2 times, as long as the word set a e have quite a number of 1, o occurred less than 2 times, then the set B All their words are certain subset.