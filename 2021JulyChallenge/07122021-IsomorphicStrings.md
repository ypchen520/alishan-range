# Isomorphic Strings

## Description

* Given two strings s and t, determine if they are isomorphic.
* Two strings s and t are isomorphic if the characters in s can be replaced to get t.
* All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## Solution

### [Hashing](https://www.educative.io/edpresso/how-to-check-if-two-strings-are-isomorphic)

* Use a hashtable to store mappings of the characters from s to those of t
* Use a set/list to keep track of already mapped characters (No two characters may map to the same character)

### Java

* HashMap
  * containsKey()
  * put(key, value)
* HashSet
  * add()
  * contains()
* String
  * char c = str.charAt(i)

### First occurence transformation

```Java
class Solution {
    private String transformString(String s) {
        Map<Character, Integer> indexMapping = new HashMap<>();
        StringBuilder builder = new StringBuilder();
        
        for (int i = 0; i < s.length(); ++i) {
            char c1 = s.charAt(i);
            
            if (!indexMapping.containsKey(c1)) {
                indexMapping.put(c1, i);
            }
            
            builder.append(Integer.toString(indexMapping.get(c1)));
        }
        return builder.toString();
    }
    
    public boolean isIsomorphic(String s, String t) {
        return transformString(s).equals(transformString(t));
    }
}
```
