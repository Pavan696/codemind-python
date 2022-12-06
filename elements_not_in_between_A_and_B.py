n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
for i in range(a,b+1):
    c.append(i)
for i in l:
    if i not in c:
        d.append(i)
if len(d)==0:
    print(-1)
else:
    print(*d)