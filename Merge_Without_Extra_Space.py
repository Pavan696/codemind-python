x=int(input())
for i in range(x):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    for k in range(n):
        b.append(a[k])
    print(*sorted(b))