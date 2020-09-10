s=input()
l=list(s)
d={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
l.reverse()
n=0
for i in range(len(l)):
    if l[i] in d.keys():
        n=n+d[l[i]]*16**i
    else:
        n=n+int(l[i])*16**i
print(n)