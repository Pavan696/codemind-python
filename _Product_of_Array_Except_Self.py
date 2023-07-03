k=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(k):
    a=[]
    s=1
    a.append(l[i])
    for j in range(k):
        if l[j] not in a:
            s*=l[j]
    b.append(s)
print(*b)