n=int(input())
a=1
b=1
c=a+b
l=[]
l.append(a)
l.append(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    l.append(c)
print(l)