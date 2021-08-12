## Binary Tree Level Order Traversal
* JAVA
  * ArrayList(class)-->implements-->List(interface)-->extends-->Collection
    * ```List<Integer> l1 = new ArrayList<Integer>(); ```
    * Array
      * Simple **fixed sized** arrays that we create in Java
    * ArrayLisy
      * **Dynamic sized** arrays in Java that implement List interface
# Solution: using two queues
* use two queues to track the current level and the next level
* queue in JAVA
  * LinkedList<TreeNode> current = new LinkedList<TreeNode>();
    * isEmpty()
    * remove(): returns the head of the list
      * Queue<TreeNode>: **poll()**
    * add()
  * add ArrayList to ArrayList<ArrayList<>>: add()
  * empty the ArrayList or LinkedList:
    * VAR = new ArrayList<>() or new LinkedList<>()
* JAVA
  * List<Integer> VAR = new ArrayList<Integer>();
  * List<List<Integer>> VAR = new ArrayList<List<Integer>>();
  * List/LinkedList 
    * length: size()
    * element: get()
  * ```continue```
* Python 
  * queue: List
    * pop and append
  * check if a list is empty: ```if not LIST:```
# Solution: using a queue
* Python
* Create an empty queue q
* temp_node = root /*start from root*/
* Loop while temp_node is not NULL
  * print temp_node->data.
  * Enqueue temp_node’s children (first left then right children) to q
  * Dequeue a node from q.
