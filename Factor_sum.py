def fac(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=i
    return c

l=list(map(int,input().split(',')))
b=[]
k=0
for i in l:
    s=fac(i)
    if s in l:
       b.append(i)
       k+=1
c=sorted(b)
if k==0:
    print(-1)
else:
    print(*c)