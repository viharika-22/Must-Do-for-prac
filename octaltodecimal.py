n=int(input())
l=[]
while n>0:
    r=n%8
    l.append(r)
    n=n//8
l.reverse()
print("".join(list(map(str,l))))