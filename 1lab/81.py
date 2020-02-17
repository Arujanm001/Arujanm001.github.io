from math import*
def distance (x1,y1,x2,y2):
    x=x2-x1
    y=y2-y1
    return (sqrt(x**2+y**2))
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
print(distance(x1,y1,x2,y2))