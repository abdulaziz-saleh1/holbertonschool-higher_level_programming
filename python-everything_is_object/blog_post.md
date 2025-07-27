# 🐍 Python3: Mutable, Immutable... Everything is Object!

![Python Object Model](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

## Introduction
In Python, everything is treated as an object — whether it's a number, string, list, or even a function. This core idea affects how variables behave, how memory is managed, and how data is passed around in functions. This post summarizes key concepts around object identity, mutability, and references in Python.

---

## `id()` and `type()`
To understand any variable in Python, use:
- `id()` to get the object’s unique identifier (memory address in CPython).
- `type()` to find out what kind of object it is.

```python
x = 10
print(id(x))     # e.g., 9785152
print(type(x))   # <class 'int'>
```

---

## Mutable Objects
Mutable objects can be changed after creation. Lists, dictionaries, and sets are all mutable types.

```python
a = [1, 2, 3]
b = a
a.append(4)
print(b)  # [1, 2, 3, 4]
```

---

## Immutable Objects
Immutable objects cannot be changed after creation. Examples include integers, floats, strings, and tuples.

```python
a = 5
b = a
a += 1
print(b)  # 5
```

---

## Why It Matters
Understanding mutability is crucial in Python because:
- Variable assignment doesn’t copy objects — it creates references.
- Mutating one variable can unexpectedly affect another.
- Python internally optimizes immutable objects like small integers and strings (interning).

```python
a = [1, 2]
b = a
a += [3]
print(b)  # [1, 2, 3]
```

---

## Argument Passing in Functions
Python uses **call-by-object-reference** (or call-by-sharing). This means:
- Mutable objects passed to a function can be changed **in place**.
- Immutable objects cannot be changed — reassignment just affects the local variable.

```python
def add_one(n):
    n += 1

x = 10
add_one(x)
print(x)  # 10

def append_one(lst):
    lst.append(1)

my_list = []
append_one(my_list)
print(my_list)  # [1]
```

---

## Conclusion
Understanding how Python handles mutable and immutable objects will help you avoid bugs and write more predictable code. Always be mindful of whether you're creating new objects or modifying existing ones — and use `id()` and `type()` to debug!
