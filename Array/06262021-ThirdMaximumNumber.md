# Third Maximum Number

## Description

* Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

## Solution

### Hashtable

* import java.util.*;
* Hashtable
* ht.keys()
* Collections.list()
* Collections.sort()

```Java
import java.util.*;
class Solution {
    public int thirdMax(int[] nums) {
        // int[] arr = new int[]{2,1,3};
        // Arrays.sort(arr);
        // for(int e: arr) System.out.println(e);
        Hashtable<Integer, Integer> ht = new Hashtable<>();
        for(int e : nums){
            ht.put(e, 0);
        }
        List<Integer> tmp = Collections.list(ht.keys());
        // System.out.println(tmp);
        Collections.sort(tmp);
        int n = tmp.size();
        if(n < 3) return tmp.get(n-1);
        return tmp.get(n-3);        
    }
}
```

### Comparison

```Java
public int thirdMax(int[] nums) {
    int max1 = Integer.MIN_VALUE;       
    int max2 = Integer.MIN_VALUE;
    int max3 = Integer.MIN_VALUE;
    boolean isMin = false;
    for(int num : nums){
        if(num == Integer.MIN_VALUE) isMin = true;
        if(num == max1 || num == max2 || num <= max3) continue;
        if(num > max1){
            max3 = max2;
            max2 = max1;
            max1 = num;
        }else if(num > max2){
            max3 = max2;
            max2 = num;
        }else{
            max3 = num;
        }
    }
    if(max2 == Integer.MIN_VALUE || max3 == Integer.MIN_VALUE && !isMin) return max1;
    return max3;
}
```
