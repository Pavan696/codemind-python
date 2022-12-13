n=int(input())
l=list(map(int,input().split()))
b=int(input())
c=[]
for i in l:
    if i not in c and l.count(i)==b:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(*c)