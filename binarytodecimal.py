n=input()
l=list(n)
l=list(map(int,l))
l.reverse()
n=0
for i in range(len(l)):
    n+=l[i]*2**i
print(n)