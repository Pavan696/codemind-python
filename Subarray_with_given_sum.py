a=int(input())
for l in range(a):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    s=0
    c=[]
    for i in range(n):
        s=0
        for j in range(i,n):
            s=s+arr[j]
            if(s==k):
                c.append((i+1,j+1))
                break
    if len(c)>0:
        print(*c[0])
    else:
        print('-1')