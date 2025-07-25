Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> t=(1,2,3,'a','b','codegnan',[4,5,6],7,1,2.5)
>>> #immutable
>>> t[0]=100
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t[0]=100
TypeError: 'tuple' object does not support item assignment
>>> 
>>> #index based slicible
>>> print(t[4])
b
>>> print(t[-4])
[4, 5, 6]
>>> print(t[2:-3:1])
(3, 'a', 'b', 'codegnan', [4, 5, 6])
>>> print(t[-2:6:1])
()
>>> print(t[-2:6:-1])
(1, 7)
>>> print(t[4:100])
('b', 'codegnan', [4, 5, 6], 7, 1, 2.5)
>>> 
>>> #empty tuple
>>> t1=()
>>> t2=tuple()
>>> t3=(1,2,3,"codegnan")
>>> t4=(56)
>>> print(type(t1),type(t2),type(t3),type(t4))
<class 'tuple'> <class 'tuple'> <class 'tuple'> <class 'int'>
>>> 
>>> #read tuple from user
>>> t=tuple(map(int, input().split()))
print(t)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    t=tuple(map(int, input().split()))
ValueError: invalid literal for int() with base 10: 'print(t)'
>>> 
>>> #tuple concatenation using '*'
>>> t1=(1,2,'hi')
>>> t2=(3,4,'bye')
>>> t3=t1+t2
>>> print(t3)
(1, 2, 'hi', 3, 4, 'bye')
>>> 
#tuple repeate using '*'
t1=(1,2,'hi')
print(t1 * 3)
(1, 2, 'hi', 1, 2, 'hi', 1, 2, 'hi')

#tuple method
#count()
t=(1,2,3,'a','b','codegnan',[1,4,5,6],7,1,,2.5)
SyntaxError: invalid syntax
t=(1,2,3,'a','b','codegnan',[1,4,5,6],7,1,2.5)
ind=t.index(1)
count_1=t.count(1)
print("index of 1 ele is:", ind)
index of 1 ele is: 0
print("count of 1 ele is :", count_1)
count of 1 ele is : 2

#build in functions()
t=(1,2,3,54,90,56,45)
min_val=min(t)
max_val=max(t)
sum_tuple=sum(t)
length=len(t)
print(min_val,max_val,sum_tuple,length)
1 90 251 7

#sorted()
t=(1,2,3,54,90,56,45)
new_t=sorted(t,reverse=False)
print(new_t)
[1, 2, 3, 45, 54, 56, 90]
