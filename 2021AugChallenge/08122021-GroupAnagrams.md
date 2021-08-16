# Group Anagrams

## Description

* Given an array of strings strs, group the anagrams together. You can return the answer in any order.
* An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Solution

### HashMap

* sort the strings such that
  * anagrams will be exactly the same
* the keys of the map are different types of anagrams
* the values of the map will be lists of anagrams with the same type
  * return new ArrayList(map.values());
  