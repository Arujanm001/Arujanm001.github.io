def gcd(a,b):
    if (b > a):
        return gcd(b,a)
    r=a%b
    if (r==0):
        return b
    else:
        return gcd(b,r)
        
x=int(input())
y=int(input())
print(gcd(x,y))