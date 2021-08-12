# Determine if Two Strings Are Close

## Description

* Two strings are considered close if you can attain one from the other using the following operations:
  * Operation 1: Swap any two existing characters.
    * For example, abcde -> aecdb
  * Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
    * For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
* You can use the operations on either string as many times as necessary.

## Solution

### Hint

* Operation 1 allows you to freely reorder the string.
* Operation 2 allows you to freely reassign the letters' frequencies.

### Python

* dict.values()
* sort
  * sort() is a method that only list objects inherit from their parent class. 
  * sorted() is a function for sorting any interable, including list . 
  * The former mutates its context list in-place and returns None , while the latter returns a copy of the argument object, sorted.
