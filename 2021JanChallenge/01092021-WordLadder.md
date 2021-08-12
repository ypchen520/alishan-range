# Word Ladder

## Description

* Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:
  * Only one letter can be changed at a time.
  * Each transformed word must exist in the word list.
* Return 0 if there is no such transformation sequence.

## Solution

### BFS

* Start from the given start word.
* Push the word in the queue
* Run a loop until the queue is empty
* Traverse all words that adjacent (differ by one character) to it and push the word in a queue (for BFS)
  * change the character at each position of the current word and see if the new word is in the given list
* Keep doing so until we find the target word or we have traversed all words.

### Python3

#### deque

* from collections import deque
* popleft()
* Deque (Doubly Ended Queue) in Python is implemented using the module “collections“. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity
* **deque.popleft() is faster than list.pop(0), because the deque has been optimized to do popleft() approximately in O(1), while list.pop(0) takes O(n)**

#### string

* 'str' object does not support item assignment
* str to list
  * list = [i for i in str]

#### set

* .add
* .remove
* SET = set(LIST)

#### dict

* dictionary.get("Age") is same as writing dictionary["Age"] or None so it implicitly handles KeyError exception

#### del

#### ord

* Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string
* This is **the inverse of chr() for 8-bit strings** and of unichr() for unicode objects

#### Python – Check if a list is empty or not

* https://www.geeksforgeeks.org/python-check-if-list-empty-not/
* if len(list) == 0
* if not list
* **numpy** (numpy.array())
  * if numpy.size:
