# Average of Levels in Binary Tree

## Description

* Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

## Solution

### **Level order traversal**

* Start by pushing the root node into the queue. Then, remove a node from the front of the queue.
* For every node removed from the queue, push all its children into a new temporary queue.
* Keep on popping nodes from the queue and adding these node’ s children to the temporary queue till queue becomes empty.
* Every time queue becomes empty, it indicates that one level of the tree has been considered.
* While pushing the nodes into temporary queue, keep a track of the sum of the nodes along with the number of nodes pushed and find out the average of the nodes on each level by making use of these sum and count values.
* After each level has been considered, again initialize the queue with temporary queue and continue the process till both queues become empty.

### Java

* Queue (interface)
  * Declaration

  ```java
  Queue<Integer> q = new LinkedList<Integer>();
  ```

  * peek()
  * poll()
* List (interface)
  * Declaration

  ```java
  List<Integer> l = new ArrayList<Integer>();
  ```

* Convert int to double
  * Double.valueOf()
  
