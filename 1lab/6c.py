import math
s=str(input())
a=len(s)
b=math.ceil(a/2)
s1=s[0:b]
s2=s[b:]
s3=s2+s1
print(s3)
