# N-ary Tree Level Order Traversal

## Description

* Given an n-ary tree, return the level order traversal of its nodes' values.
* Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

## Solution

### Queque

### Java

* queue
  * offer():
    * add()
    * [the add method throws an exception](https://stackoverflow.com/questions/2703984/what-is-the-difference-between-the-add-and-offer-methods-in-a-queue-in-java)
  * poll()
    * This method **returns** and **removes** the element at the front of the container or the head of the Queue. 
    * The method **does not throws an exception** when the Queue is empty, it returns **null** instead.
  * isEmpty()

```Java
Queue<> q = new LinkedLisk<>();
!q.isEmpty()
q.offer();
q.poll();
```
