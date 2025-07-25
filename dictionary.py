Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#keys
d={'language':'python','version':'3.13.5','level':'high level'}
keys=d.keys()
print(keys)
dict_keys(['language', 'version', 'level'])
#values
values=d.values()
print(values)
dict_values(['python', '3.13.5', 'high level'])
items=d.items()
print(items)
dict_items([('language', 'python'), ('version', '3.13.5'), ('level', 'high level')])

#type conversion
d={'language':'python','version':'3.13.5','level':'high level'}
items=d.items()
print(type(items))
<class 'dict_items'>
print(items)
dict_items([('language', 'python'), ('version', '3.13.5'), ('level', 'high level')])
items_list=list(items)
print(type(items_list))
<class 'list'>
print(items_list)
[('language', 'python'), ('version', '3.13.5'), ('level', 'high level')]

a,b=items_list[1]
print(a,b)
version 3.13.5

#pop key
d={'language':'python','version':'3.13.5','level':'high level'}
val=d.pop('version')
print(val)
3.13.5
print(d)
{'language': 'python', 'level': 'high level'}

#pop item
d={'language':'python','version':'3.13.5','level':'high level'}
item=d.popitem()
print(item)
('level', 'high level')
print(d)
{'language': 'python', 'version': '3.13.5'}

#accessing and updating the value
d={'language':'python','version':'3.13.5','level':'high level'}
print(d['language'])
python

d['A']=1
d['language']='java'
>>> print(d)
{'language': 'java', 'version': '3.13.5', 'level': 'high level', 'A': 1}
>>> 
>>> #get(key,default)
>>> d={'language':'python','version':'3.13.5','level':'high level'}
>>> val=d.get('version','key is not in dictionary')
>>> print(val)
3.13.5
>>> 
>>> val=d.get('z','key is not in dictionary')
>>> print(val)
key is not in dictionary
>>> 
>>> d={'language':'python','version':'3.13.5','level':'high level'}
>>> val=d.get('z')
>>> print(val)
None
>>> 
>>> d={'language':'python','version':'3.13.5','level':'high level'}
>>> val=d.get('z',10)
>>> print(val)
10
>>> 
>>> #update(dictionary)
>>> d1={'language':'python','version':'3.13.5','level':'high level'}
>>> d2={'language':'java','level':'high level'}
>>> d1.update(d2)
>>> print(d1)
{'language': 'java', 'version': '3.13.5', 'level': 'high level'}
>>> print(d2)
{'language': 'java', 'level': 'high level'}
>>> d2.update(d1)
>>> print(d2)
{'language': 'java', 'level': 'high level', 'version': '3.13.5'}
>>> print(d1)
{'language': 'java', 'version': '3.13.5', 'level': 'high level'}
>>> 
>>> #clear
>>> d1={'language':'python','version':'3.13.5'}
>>> d1.clear()
>>> print(d1)
{}
>>> 
>>> d={'a':[1,2,3,4],3:[40,5,6,7]}
>>> d[3][0]
40
