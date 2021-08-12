# Maximum Frequency Stack

## Description

* Implement FreqStack, a class which simulates the operation of a stack-like data structure.
* FreqStack has two functions:
  * push(int x), which pushes an integer x onto the stack.
  * pop(), which removes and returns the most frequent element in the stack.
    * If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.

## Solution

### Hash Map

* Maitain frequency map and bucket of stacks
  * frequency map: {'int': 'count'}
  * bucket of stacks: {'count': 'Stack<>'}
* Keep track of the maximum frequency

```java
private int maxFreq
```
