# Reduce Array Size to The Half

## Description

* Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.
* Return the minimum size of the set so that at least half of the integers of the array are removed.

## Solution

### Hint

* Count the frequency of each integer in the array.
* Start with an empty set, add to the set the integer with the maximum frequency.
* Keep Adding the integer with the max frequency until you remove at least half of the integers.

### Java

* Hashing
  * Map

    ``` Java
    Map<Integer, Integer> mp = new HashMap<>();
    for (int i = 0; i < n; i++){
        if (mp.containsKey(arr[i]))
        {
            mp.put(arr[i], mp.get(arr[i]) + 1);
        }
        else
        {
            mp.put(arr[i], 1);
        }
    }
    // Traverse through map and print frequencies
    for (Map.Entry<Integer, Integer> entry : mp.entrySet())
    {
        System.out.println(entry.getKey() + " " + entry.getValue());
    }
    mp.keySet();
    ```

* Set

  ```Java
  Set<String> hs = new HashSet<String>();
  hs.add("Hello");
  ```

* Priority Queue

  ```Java
  PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> (int) (mp.get(o2) - mp.get(o1)));
  pq.addAll(mp.keySet());
  mp.get(pq.poll()); //The peek() method only retrieved the element at the head but the poll() also removes the element along with the retrieval. It returns NULL if the queue is empty
  ```
