# Palindrome Partitioning II

## Description

* Given a string s, partition s such that every substring of the partition is a palindrome.
* Return the minimum cuts needed for a palindrome partitioning of s.

## Solution

### [DP](https://www.programcreek.com/2014/04/leetcode-palindrome-partitioning-ii-java/)

* Two arrays
  * one tracks the partition position: dp(i,j)
  * the other tracks the number of minimum cut: cut(j)
* dp(i,j)
  * whether or not the substring starting with position i and ending with position j is a palindrome
* cut(j)
  * minimum cuts for the substring s[0 .. j]
  