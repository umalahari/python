Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='abcdefg'
print(s[5])
f

#string slicing
print(s[0:5])
abcde
print(s[ :-3])
abcd
>>> print(s[ : :-2])
geca
>>> 
>>> #string reversal using slicing
>>> print(s[ : :-1])
gfedcba
>>> print(s[0:2:1])
ab
>>> 
>>> #string concatenation using "+"
>>> string1="uma"
>>> string2="lahari"
>>> print(string1+ " "+string2)
uma lahari
>>> s1="welcome"
>>> s2="to"
>>> s3="code gnan"
>>> print(s1+ " "+s2+ " "+s3)
welcome to code gnan
>>> 
>>> #string repetation using "*"
>>> word="lahari"
>>> print("word "*3)
word word word 
>>> print(" "word * 3)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> 
>>> #removing whitespaces
>>> text="@@@@@@lahari@@@@@"
>>> print(text.strip())
@@@@@@lahari@@@@@
>>> print(text.lstrip())
@@@@@@lahari@@@@@
>>> print(text.rstrip())
@@@@@@lahari@@@@@
>>> 
>>> #string case coversion
>>> strings="umalahari"
>>> print(strings.lower())
umalahari
>>> print(strings.upper())
UMALAHARI
>>> print(strings.swapcase())
UMALAHARI
>>> print(strings.title())
Umalahari
>>> print(strings.capitalize())
Umalahari

#split string
char="I am a codegnan student"
print(string.split())
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(string.split())
NameError: name 'string' is not defined. Did you mean: 'string1'? Or did you forget to import 'string'?
print(char.split())
['I', 'am', 'a', 'codegnan', 'student']
print(char.split('a'))
['I ', 'm ', ' codegn', 'n student']
print(char.split('z'))
['I am a codegnan student']

#string joining
#sub string methods
character="I am a good girl"
print(character.find("a"))
2
print(character.index("z"))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(character.index("z"))
ValueError: substring not found
print(character.replace("a","b"))
I bm b good girl

#string checking functions
name1="abcdefg"
name2="1234567"
name3="123ab"
name4="abc@123"
print(name1.isalpha(),name1.isdigit(),name1.isalnum())
True False True

#string comparision
l1='abcde'
l2='abcdef'
print(l1>l2)
False
print(l1<l2)
True
