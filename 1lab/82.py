def min(a,b):
    if a<b:
        return a
    else:
        return b
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(min(min(a,b),min(c,d)))