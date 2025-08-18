Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#creating a set
s={1,2,3,'codeganan','A',4.5}
print(s)
{1, 2, 'codeganan', 'A', 4.5, 3}

#creating empty set
s1={}
s2=set()
print(type(s1),type(s2))
<class 'dict'> <class 'set'>

#set allows unique values
s={1,2,3,4,2,3}
print(s)
{1, 2, 3, 4}

#read set of integers from user
s=set(map(str, input().split()))
print(s)
1,2,3,4,5,6
(1, 2, 3, 4, 5, 6)

#operation on sets

#union
s1={1,2,3,4}
s2={3,4,5,6}
union=s1.union(s2)
print(union)
{1, 2, 3, 4, 5, 6}

#intersection
intersection=s1.intersection(s2)
print(intersection)
{3, 4}

#difference
difference=s1.difference(s2)
print(difference)
{1, 2}

#symmetric_difference
symmetric_difference=s1.symmetric_difference(s2)
print(symmetric_difference)
{1, 2, 5, 6}

#subset
s1={1,2,3,4,5,6}
s2={4,6}
print(s1.issubset(s2))
False

print(s2.issubset(s1))
True

#superset
print(s1.issuperset(s2))
True
>>> 
>>> #disjoint
>>> print(s1.disjoint(s2))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(s1.disjoint(s2))
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> print(s1.isdisjoint(s2))
False
>>> 
>>> #set methods
>>> s={1,2,3,4}
>>> print("original set:",s)
original set: {1, 2, 3, 4}
>>> 
>>> s.add(100)
>>> print("after add operation:",s)
after add operation: {1, 2, 3, 100, 4}
>>> 
>>> #update
>>> s.update([1,2,3])
>>> print("after update operation:",s)
after update operation: {1, 2, 3, 100, 4}
>>> 
>>> #remove
>>> s.remove(2)
>>> print("after remove operation:",s)
after remove operation: {1, 3, 100, 4}
>>> 
>>> #discard
>>> s.update([20,30])
>>> print(s)
{1, 3, 100, 4, 20, 30}
>>> s.discard(20)
>>> print("after discard operation:",s)
after discard operation: {1, 3, 100, 4, 30}
>>> 
>>> #pop
>>> s.pop()
1
>>> 
>>> #clear
>>> s.clear()
>>> print(s)
set()
