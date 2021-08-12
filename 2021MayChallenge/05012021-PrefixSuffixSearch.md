# Prefix and Suffix Search

## Description

* Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.
* Implement the WordFilter class:
  * WordFilter(string[] words) Initializes the object with the words in the dictionary.
  * f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix and the suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1

## [Solution](https://github.com/grandyang/leetcode/issues/745)

### Hint

* For a word like "test", consider "#test", "t#test", "st#test", "est#test", "test#test". Then if we have a query like prefix = "te", suffix = "t", we can find it by searching for something we've inserted starting with "t#te".
