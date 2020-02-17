from math import *
n=int(input())
a=1
b=2
for i in range (2,n+1):
    a=a+(1/b**2)
    b=b+1
print (a)