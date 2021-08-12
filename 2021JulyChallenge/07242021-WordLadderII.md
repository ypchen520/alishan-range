# Word Ladder II

## Description

* A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
  * Every adjacent pair of words differs by a single letter.
  * Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
  * sk == endWord
* Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

## Solution

### [BFS + DFS](https://zxi.mytechroad.com/blog/searching/leetcode-126-word-ladder-ii/)

* if word list does not contain endWord: return null
* use BFS to contruct the graph and use DFS to extract the paths
