def row_sor(l):
    m=sorted(l)
    n=sorted(l,reverse=True)
    return l==m or l==n
a,b=map(int,input().split())
s=0
for i in range(a):
    x=list(map(int,input().split()))
    if row_sor(x):
        s+=1
print(s)