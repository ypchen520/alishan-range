# Recurrence Relation

* recurrence relation
* base case
* Next
  * avoid duplicate calculations

## Pascal's Triangle

```Java
private static int calculatePascalsTriangle(int r, int c){
    if(c > r) return -1;
    return helper(r,c);
}

private static int helper(int r, int c){
    if(c == 1 || r == c) return 1;
    return helper(r-1, c-1) + helper(r-1, c);
}
```

### iterative

```Java
List<List<Integer>> res = new ArrayList<>();
List<Integer> row = new ArrayList<>();
for(int i = 0; i < numRows; i++){
    row.add(0, 1);
    for(int j = 1; j < i; j++){
        row.set(j, row.get(j)+row.get(j+1));
    }
    res.add(new ArrayList<>(row));
}
return res;
```