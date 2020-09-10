def cal_gcd(a,b):
    while b:
        a,b=b,a%b
    return a
n=list(map(int,input().split()))
n.sort()
a=n[0]
b=n[1]
c=cal_gcd(a,b)
for i in range(2,len(n)):
    c=cal_gcd(c,n[i])
print(c)