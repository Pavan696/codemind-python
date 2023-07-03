a,b = map(int,input().split())
l1=[]
for i in range(a):
    l=list(map(int,input().split()))
    l1.append(l)
s1=[]
for j in range(b):
    s=0
    for i in range(a):
        s+=l1[i][j]
    s1.append(s)
print(max(s1))