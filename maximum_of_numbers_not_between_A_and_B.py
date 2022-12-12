n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=[]
e=0
for i in range(a,b+1):
    c.append(i)
for i in l:
    if i not in c:
        d.append(i)
        e+=1
if e==0:
    print(-1)
else:
    print(max(d))