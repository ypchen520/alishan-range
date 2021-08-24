my_tuple = ("a", 1, "b")
print(type(my_tuple))
my_str = ("a")
my_str_tuple = ("a",)
print(f'("a") is a string: {type(my_str)}')
print(f'("a",) is a tuple: {type(my_str_tuple)}')

my_tuple = tuple(['a', 1, 'b', 'a', 'b'])

print(type(my_tuple[1]))
print(type(my_tuple[0]))

for x in my_tuple:
    print(x)

if "a" in my_tuple:
    print("yes")
else:
    print("no")

print(f"number of elements: {len(my_tuple)}")
print(f"number of 'a': {my_tuple.count('a')}")
print(f"first index of 'b': {my_tuple.index('b')}")

my_list = list(my_tuple)
print(my_list)

my_tuple_2 = tuple(my_list)
print(my_tuple_2)

my_tuple_3 = (1,2,3,4,5,6,7,8,9)

print(my_tuple_3[:5])
print(my_tuple_3[2:5])
print(my_tuple_3[2:])
print(my_tuple_3[::-1])
print(my_tuple_3[::2])