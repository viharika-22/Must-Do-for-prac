n=int(input())
l=[]
while n>0:
    r=n%2
    l.append(r)
    n=n//2
l.reverse()
print("".join(list(map(str,l))))