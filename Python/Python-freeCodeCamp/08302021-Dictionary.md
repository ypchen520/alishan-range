# Dictionary

* a collection data type
  * key-value pairs
  * unordered
  * mutable
  * {}
* declare
  * dict()
* access
* add
* delete
  * del
  * pop()
  * popitem(): the last inserted
* containsKey
  * if key in dict
* loop through
  * for key in dict
  * dict.keys()
  * dict.values()
  * dict.items()
* copy
  * dict.copy()
  * dict()
* merge two dictionaries
  * update()
* tuple can also be a key (has to be immutable)
  
  ```Python
  my_tuple = (5,20)
  my_tuple_dict = {my_tuple: 1992}
  ```

```Python
my_dict = {"name": "Dennis", "age": 29, "city": "GNV"}

my_dict2 = dict(name="yupeng", age=29, city="hsinchu")
print(my_dict2)

my_dict["email"] = "ypchen520@gmail.com"
print(my_dict)

# del my_dict2["name"]
# print(my_dict2)
# my_dict.popitem()
# print(my_dict)

if "name" in my_dict2:
        print(my_dict2["name"])

try:
    print(my_dict2["name"])
except:
    print("Error")

for key in my_dict:
    print(key)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

my_dict_cpy = my_dict.copy()
my_dict_cpy2 = dict(my_dict)

print(f"before updating my_dict with my_dict2: {my_dict}")
my_dict.update(my_dict2)
print(f"after updating my_dict with my_dict2: {my_dict}")

my_tuple = (5,20)
my_tuple_dict = {my_tuple: 1992}
print(my_tuple_dict)
```
