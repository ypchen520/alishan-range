# Longest String Chain

## Description

* Given a list of words, each word consists of English lowercase letters.
* Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".
* A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
* Return the longest possible length of a word chain with words chosen from the given list of words.

## Solution

### Hint

* Instead of adding a character, try deleting a character to form a chain in reverse.
* For each word in order of length, for each word2 which is word with one character removed, length[word2] = max(length[word2], length[word] + 1).

### DP

### TypeScript (JavaScript)

* Sort an array based on the length of each element:

```JavaScript
arr.sort(function(a, b){
  // ASC  -> a.length - b.length
  // DESC -> b.length - a.length
  return b.length - a.length;
});
```

### Python

* Sort an array based on the length of each element:

```Python
for w in sorted(words, key=len):
```
