n=input()
l=list(n)
l=list(map(int,l))
o=0
for i in range(len(l)):
    o+=l[i]*8**i
b=[]
while o>0:
    r=o%2
    b.append(r)
    o=o//2
print("".join(list(map(str,b))))