# Encode and Decode TinyURL

## Description

* TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
* Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

## Solution

```Java
HashMap<String, String> longToShort = new HashMap<String, String>();
HashMap<String, String> shortToLong = new HashMap<String, String>();
seed = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
```

* Java
  * StringBuilder vs. String
    * StringBuilder
      * represents a mutable sequence of characters
    * String
      * the String Class in Java creates an immutable sequence of characters
  * [Immutable](https://www.baeldung.com/java-string-immutable)
    * An immutable object is an object whose internal state remains constant after it has been entirely created. This means that once the object has been assigned to a variable, we can neither update the reference nor mutate the internal state by any means.
    * String
      * The key benefits of keeping this class as immutable are caching, security, synchronization, and performance.
      