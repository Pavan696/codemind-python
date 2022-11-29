a,b=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
p=[]
m=[]
n=[]
for i in l:
    if i not in k:
        m.append(i)
    else:
        p.append(i)
for i in k:
    if i not in l:
        m.append(i)
    else:
        p.append(i)
print(*m)