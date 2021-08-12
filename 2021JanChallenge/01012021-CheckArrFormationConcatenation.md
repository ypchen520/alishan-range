# Check Array Formation Through Concatenation

## Description

* You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. 
* Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
* Return true if it is possible to form the array arr from pieces. Otherwise, return false

## Solution

* make the array a string with delimiters
  * [1,2,3,4]
  * #1#2#3#4#
* Python
  * string
    * ''.join(LIST)
    * contains
      * if "sub_STR" not **in** STR: 
        * continue
      * find, index
