n1=int(input())
n2=int(input())
l=[]
am=[]
for i in range(n1,n2+1):
    l.append(i)
for i in range(len(l)):
    a=0
    b=l[i]
    p=len(str(l[i]))
    while l[i]>0:
        r=l[i]%10
        a=a+r**p
        l[i]=l[i]//10
    if b==a:
        am.append(b)
print(am)