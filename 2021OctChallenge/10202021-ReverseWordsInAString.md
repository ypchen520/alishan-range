# Reverse Words in a String

## Description

* Given an input string s, reverse the order of the words.

* A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
* Return a string of the words in reverse order concatenated by a single space.
* Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Solution

### Two-pointer

* reverse the entire string
* reverse each word
* clean up spaces

```JAVA
private void reverse(char[] arr, int i, int j){
    while(i < j){
        char tmp = arr[i];
        arr[i++] = arr[j];
        arr[j--] = tmp;
    }
}
```