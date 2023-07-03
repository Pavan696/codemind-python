a=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(a):
    t=set(l)
    t.discard(l[i])
    s=1
    for i in t:
        s*=i
    b.append(s)
print(*b)
    

