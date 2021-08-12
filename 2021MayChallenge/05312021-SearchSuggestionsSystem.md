# Search Suggestions System

## Description

* Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
* Return list of lists of the suggested products after each character of searchWord is typed. 

## Solution

### Hint

* Brute force is a good choice because length of the string is ≤ 1000.
* Binary search the answer.
* Use Trie data structure to store the best three matching. Traverse the Trie.

### Binary Search

### Trie + DFS
