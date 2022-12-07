a=int(input())
l=list(map(int,input().split()))
k=0
c=[]
for i in l:
    if l.count(i)==1:
        c.append(i)
        k+=1
if k==0:
    print(-1)
else:
    print(*c)