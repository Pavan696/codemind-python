a=int(input())
for i in range(a):
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for i in range(n):
        if a[i]%2!=0:
            s+=1
    print(s//2)