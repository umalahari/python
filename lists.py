Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> lst=[1,2,3,'hi','a','b',23.5,1,2]
>>> lst[0]
1
>>> lst[-1]
2
>>> 
>>> #mutable operation
>>> lst[0]=1000
>>> print(lst)
[1000, 2, 3, 'hi', 'a', 'b', 23.5, 1, 2]
>>> 
>>> #creating empty list
>>> lst=[]
>>> lst1=list()
>>> print(type(lst))
<class 'list'>
>>> print(type(lst1))
<class 'list'>
>>> 
>>> #string to list type
>>> s="umalahari"
>>> l=list(s)
>>> print(type(s),type(l))
<class 'str'> <class 'list'>
>>> print(l)
['u', 'm', 'a', 'l', 'a', 'h', 'a', 'r', 'i']
>>> 
>>> #reading list of integers from user
>>> lst=list(map(int, input().split()))
print(lst)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    lst=list(map(int, input().split()))
ValueError: invalid literal for int() with base 10: 'print(lst)'
>>> 
>>> #reading list of float
>>> #list concatination
>>> l1=[1,2,3]
>>> l2=[4,5,6]
>>> print(l1+l2)
[1, 2, 3, 4, 5, 6]
>>> 
>>> #list repeatation using '*'
>>> l1=[1,2,3]
>>> print(l1 * 4)
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#list methods
#append
l=[1,2,3,5.5,'a','b',1,2,3]
l.append(100)
print("after append operation: ",1)
after append operation:  1
print("after append operation: ",l)
after append operation:  [1, 2, 3, 5.5, 'a', 'b', 1, 2, 3, 100]

#extend
l.extend([200,300])
print("after extend operation:" ,l)
after extend operation: [1, 2, 3, 5.5, 'a', 'b', 1, 2, 3, 100, 200, 300]

#insert
l.insert(4,'codegnan')
print("after insert operation:", l)
after insert operation: [1, 2, 3, 5.5, 'codegnan', 'a', 'b', 1, 2, 3, 100, 200, 300]

#remove
l=[1,2,3,5.5,'codegnan','a','b',1,2,3]
print("original list:", l)
original list: [1, 2, 3, 5.5, 'codegnan', 'a', 'b', 1, 2, 3]
l.remove(3)
print(l)
[1, 2, 5.5, 'codegnan', 'a', 'b', 1, 2, 3]

#pop
l.pop()
3
print("after pop operation:", l)
after pop operation: [1, 2, 5.5, 'codegnan', 'a', 'b', 1, 2]
after pop operation: [1, 2, 5.5, 'codegnan', 'a', 'b', 1, 2]
SyntaxError: invalid syntax
#clear
l.clear()
print("after clear operation:", l)
after clear operation: []

#min(), max(),sum()
l=[1,2,3,29,43,3,10,200]
min_val=min(l)
max_val=max(l)
sum_list=sum(l)
print("min value in the list:", min_val)
min value in the list: 1
print("max value in the list:", max_val)
max value in the list: 200
print("sum of the list:" ,sum_list)
sum of the list: 291

#reverse()
l=[1,2,29,43,3,10,200]
l.reverse()
print("reverse of list:",l)
reverse of list: [200, 10, 3, 43, 29, 2, 1]

#sorting()
#ascending order sort
l=[1,2,29,43,3,10,200]
l.sort()
print(l)
[1, 2, 3, 10, 29, 43, 200]

#descending order
l.sort(reverse = True)
print(l)
[200, 43, 29, 10, 3, 2, 1]

#sorted()
l=[1,2,29,43,3,10,200]
new_list=sorted(l)
print(new_list)
[1, 2, 3, 10, 29, 43, 200]

#count()
l=[1,2,3,10,29,43,200,23,2,3,2]
count_2=l.count(2)
print("total 2 element count:", count_2)
total 2 element count: 3

#index()
ind=l.index(29)
print("29 value index:", ind)
29 value index: 4

#length of a list
length=len(l)
print(length)
11
