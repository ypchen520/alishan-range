# Custom Sort String

## Description

* order and str are strings composed of lowercase letters. In order, no letter occurs more than once.
* order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.
* Return any permutation of str (as a string) that satisfies this property.

## Solution

### [Counting](https://ttzztt.gitbooks.io/lc/content/sort/bucket-sort/custom-sort-string.html)

* count each char in str

### Java

* Array
  * By default, when we create an array of something in Java all entries will have its default value. For primitive types like int , long , float the default value are zero ( 0 or 0.0 ). For reference types (anything that holds an object in it) will have null as the default value. For boolean variable it will be false
* str.toCharArray()
* StringBuilder sb = new StringBuilder();
  * sb.append(char);
  * sb.toString()
