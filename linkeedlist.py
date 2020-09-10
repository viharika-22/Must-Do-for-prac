def cal_hcf(a,b):
    while b:
        a,b=b,a%b
    return a
l=list(map(int,input().split()))
l.sort()
a=l[0]
b=l[1]
hcf=cal_hcf(a,b)
p=1
for i in range(2,len(l)):
    hcf=cal_hcf(hcf,l[i])
for i in range(len(l)):
    p=p*l[i]
print(hcf)
lcm=p//hcf
print(lcm)
