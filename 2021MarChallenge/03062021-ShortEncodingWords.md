# Short Encoding of Words

## Description

* A valid encoding of an array of words is any reference string s and array of indices such that:
  * words.length == indices.length
  * The reference string s ends with the '#' character.
  * For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i]
* Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

## Solution

### Hash Set

* Add each word in the words list to a HashSet
  * remove all the possible suffix of each word
  * E.g.,
    * For "time", remove "ime", "me", and "i".
* Answer is the sum of the lengths of the words left in the HashSet
* Java
  * Initialize hashset with array
  
  ```java
  Set<String> hs = new HashSet<>(Arrays.asList(words));
  ```

### Prefix and Suffix
