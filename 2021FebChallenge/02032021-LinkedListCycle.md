# Linked List Cycle

## Description

* Given head, the head of a linked list, determine if the linked list has a cycle in it

## Solution

### Hash Table

* we can check whether a node had been visited before
* We go through each node one by one and record each node's reference (or memory address) in a hash table
* If the current node is null, we have reached the end of the list and it must not be cyclic. If current node’s reference is in the hash table, then return true.
* JAVA
  * HashSet
    * The HashSet class implements the Set interface, backed by a hash table which is actually a HashMap instance
    * The underlying data structure for HashSet is Hashtable
    * As it implements the Set Interface, duplicate values are not allowed
    * NULL elements are allowed in HashSet
    * HashSet<String> hs = new HashSet<String>();
      * Set<String> hs = new HashSet<String>();
      * hs.add("Geek"); 
      * hs.contains("Geek");
* Time complexity: O(n)
  * Adding a node to the hash table costs only O(1) time.
* Space complexity: O(n)
* Python
  * We can use set()
  * set.add()

### O(1) memory

* Floyd's Cycle Finding Algorithm
  * by considering two pointers at different speed - a slow pointer and a fast pointer
  * If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.
  * Consider a cyclic list, the fast runner will eventually meet the slow runner.
