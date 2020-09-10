n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(0,i+1):
        print(i+1,end=' ')
    print()
for i in range(n-1,0,-1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(0,i):
        print(i,end=" ")
    print()