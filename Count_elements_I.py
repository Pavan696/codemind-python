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
for i in p:
    if i not in n:
        n.append(i)
print(len(n))