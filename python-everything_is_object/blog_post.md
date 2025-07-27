Python3: Mutable, Immutable... Everything is Object!

Introduction

In Python, everything is an object. From numbers and strings to functions and classes, Python treats all values as objects with a type and identity. Understanding how Python handles these objects under the hood—particularly with respect to mutability and assignment—is essential for writing robust and predictable code.

id and type

Python provides two built-in functions to inspect any object:

id(): returns the unique identity of an object (its memory address in CPython).

type(): returns the type/class of the object.

x = 42
print(id(x))       # Might print: 9785152
print(type(x))     # <class 'int'>

Mutable Objects

Mutable objects can be changed after they are created. Built-in mutable types include:

list

dict

set

Example:

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)  # [1, 2, 3, 4] — because both refer to the same object

Immutable Objects

Immutable objects cannot be changed after creation. Examples include:

int

str

tuple

Modifying an immutable object actually creates a new one:

a = 10
b = a
a += 1
print(b)  # 10 — b still points to the original 10

Why It Matters

Understanding mutability helps prevent bugs, especially in assignment and comparison. For instance:

list1 = [1, 2, 3]
list2 = list1
list1 += [4]
print(list2)  # [1, 2, 3, 4] — still points to the same object

However:

list1 = [1, 2, 3]
list2 = list1
list1 = list1 + [4]  # creates a new object for list1
print(list2)  # [1, 2, 3]

Function Arguments: Mutable vs Immutable

Python passes variables to functions by object reference. What changes is whether the object itself is mutable:

Mutable object:

def modify(lst):
    lst.append(100)

my_list = [1, 2, 3]
modify(my_list)
print(my_list)  # [1, 2, 3, 100]

Immutable object:

def increment(n):
    n += 1

x = 5
increment(x)
print(x)  # 5

Conclusion

Whether you're working with numbers or complex data structures, understanding Python's object model is key. Remember:

Use id() and type() to inspect objects.

Know when objects are shared or copied.

Mutable types can lead to unexpected side-effects if you're not careful.

Functions modify mutable arguments in-place, but not immutable ones.

This knowledge is essential not just for Python interviews but also for writing efficient and bug-free Python code.
