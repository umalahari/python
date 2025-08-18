Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#integer to float conversion
num=24
print(float(num))
24.0

num=24
float_num=float(num)
print(type(float_num))
<class 'float'>
print(float_num)
24.0

#float to int,string conversion
num=24.0
number=int(num)
print(type(number))
<class 'int'>
print(number)
24
print(str(num))
24.0

#string to integer,float,list,tuple,set
s1='123'
s2='abc12a'
print(int(s1))
123
print(float(s1))
123.0
print(list(s2))
['a', 'b', 'c', '1', '2', 'a']
print(tuple(s2))
('a', 'b', 'c', '1', '2', 'a')
print(set(s2))
{'a', '2', 'c', 'b', '1'}
>>> print(set(s1))
{'1', '3', '2'}
>>> 
>>> #list to set,tuple and string
>>> lst=[1,2,3,'a','b',1,2]
>>> print(set(lst))
{1, 2, 3, 'a', 'b'}
>>> print(tuple(lst))
(1, 2, 3, 'a', 'b', 1, 2)
>>> print(str(lst))
[1, 2, 3, 'a', 'b', 1, 2]
>>> 
>>> #list of tuple to dictionary
>>> l=[('a',1),('b',2).('c',(1,2,3))]
SyntaxError: invalid syntax
>>> l=[('a',1),('b',2),('c',(1,2,3))]
>>> print(dict(l))
{'a': 1, 'b': 2, 'c': (1, 2, 3)}
>>> 
>>> #dictionary to list
>>> d={'a':1,'b':2,'c':(1,2,3)}
>>> print(list(d))
['a', 'b', 'c']
>>> 
>>> #tuple to list,set,string
>>> t=(1,3.'codegnan',55)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> t=(1,3,'codegnan',55)
>>> print(list(t))
[1, 3, 'codegnan', 55]
>>> print(set(t))
{1, 3, 'codegnan', 55}
>>> print(str(t))
(1, 3, 'codegnan', 55)
>>> 
>>> #set to list,tuple and string
>>> s={'codegnan',1,3,55}
>>> print(list(s))
[1, 3, 'codegnan', 55]
>>> print(tuple(s))
(1, 3, 'codegnan', 55)
>>> print(str(s))
{1, 3, 'codegnan', 55}
>>> print(str(num)+ ' abc')
24.0 abc
