Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> x=[1,2,3]
>>> print(id(x))
2759080003584
>>> y=x
>>> print(id(y))
2759080003584
>>> z=[1,2,3]
>>> print(id(z))
2759079952192
>>> print("x is y:",x is y)
x is y: True
>>> print("x is z:",x is z)
x is z: False
>>> print("x == z:",x == z)
x == z: True
>>> print("y == z:",y == z)
y == z: True
