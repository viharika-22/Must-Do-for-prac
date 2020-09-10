n=input()
l=list(n)
l=list(map(int,l))
l.reverse()
b=0
for i in range(len(l)):
    b+=l[i]*2**i
o=[]
while b>0:
    r=b%8
    o.append(r)
    b=b//8
o.reverse()
print("".join(list(map(str,o))))