n=input()
l=list(n)
l=list(map(int,l))
l.reverse()
f=0
for i in range(len(l)):
    f+=l[i]*8**i
print(f)