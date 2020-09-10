n=int(input())
l=[]
i=1
for j in range(1,n+1):
    c=0
    for k in range(1,i+1):
        a=i%j
        if a==0:
            c+=1
    if (c==2):
        l.append(i)
    else:
        k=k-1
    i=i+1
print(l)