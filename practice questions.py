Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#write a python program to convert kilometr to miles?
k=float(input())
10
to_miles=k* (1/1.609)
print(to_miles)
6.215040397762586

#miles to kilometers
miles=float(input())
15
to_kilo=miles*1.609
print(to_kilo)
24.134999999999998

#write a python program to convert celsius to fahernheit?
cel=float(input())
40
far=cel*(9/5)+32
print(far)
104.0

#fahernheit to celsius
f=float(input())
105
cel=(f-32)*5/9
print(cel)
40.55555555555556

f=float(input())
96.8
cel=(f-32)*5/9
print(cel)
36.0

#write a python program to display calender?
import calendar
year=int(input())
2025
month=int(input())
7
print(calendar.month(year,month))
     July 2025
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31


#to print year calendar/
print(calendar.calendar(year))
                                  2025

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                      1  2
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       3  4  5  6  7  8  9
13 14 15 16 17 18 19      10 11 12 13 14 15 16      10 11 12 13 14 15 16
20 21 22 23 24 25 26      17 18 19 20 21 22 23      17 18 19 20 21 22 23
27 28 29 30 31            24 25 26 27 28            24 25 26 27 28 29 30
                                                    31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                1  2  3  4                         1
 7  8  9 10 11 12 13       5  6  7  8  9 10 11       2  3  4  5  6  7  8
14 15 16 17 18 19 20      12 13 14 15 16 17 18       9 10 11 12 13 14 15
21 22 23 24 25 26 27      19 20 21 22 23 24 25      16 17 18 19 20 21 22
28 29 30                  26 27 28 29 30 31         23 24 25 26 27 28 29
                                                    30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6                   1  2  3       1  2  3  4  5  6  7
 7  8  9 10 11 12 13       4  5  6  7  8  9 10       8  9 10 11 12 13 14
14 15 16 17 18 19 20      11 12 13 14 15 16 17      15 16 17 18 19 20 21
21 22 23 24 25 26 27      18 19 20 21 22 23 24      22 23 24 25 26 27 28
28 29 30 31               25 26 27 28 29 30 31      29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2       1  2  3  4  5  6  7
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       8  9 10 11 12 13 14
13 14 15 16 17 18 19      10 11 12 13 14 15 16      15 16 17 18 19 20 21
20 21 22 23 24 25 26      17 18 19 20 21 22 23      22 23 24 25 26 27 28
27 28 29 30 31            24 25 26 27 28 29 30      29 30 31


'
#write a python program to solve quadratic equation?
import math
>>> a=int(input())
4
>>> b=int(input())
5
>>> c=int(input())
2
>>> q1=(-b-(math.sqrt(b))-4*a*c)/(2*a)
>>> print(q1)
-4.904508497187473
>>> q2=(-b+(math.sqrt(b))-4*a*c)/(2*a)
>>> print(q2)
-4.345491502812527
>>> 
>>> a,b,c=map(int, input().split())
3 -5 2
>>> val=((b**2)-(4*a*c))**0.5
>>> deno=2*a
>>> root1=(-b +val)/deno
>>> root2=(-b - val)/deno
>>> print(root1)
1.0
>>> print(root2)
0.6666666666666666
>>> 
>>> #write a python program to swap to variable without temp variable?
>>> a=int(input())
10
>>> b=int(input())
5
>>> a=a-b
>>> b=a+b
>>> a=b-a
>>> print(a,b)
5 10
>>> 
>>> a=int(input())
15
>>> b=int(input())
10
>>> a,b=b,a
>>> print(a,b)
10 15
>>> print(a)
10
>>> print(b)
15
