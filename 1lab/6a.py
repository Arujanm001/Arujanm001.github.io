s=str(input())
a=len(s)
print(s[2])
print(s[-2])
print(s[0:5])
print(s[0:a-2])
for i in range(1,a+1):
	if i%2==1:
		print(s[i-1],sep='',end='')
print('')
for i in range(1,a+1):
	if i%2==0:
		print(s[i-1],sep='',end='')
print('')
for i in range(-1,-a-1,-1):
	print(s[i],sep='',end='')
print('')
for i in range(-1,-a-1,-2):
	print(s[i],sep='',end='')
print('')
print(a)
