a=int(input())
l=list(map(int,input().split()))
r=[]
for i in l:
    if i not in r:
        r.append(i)
d=sum(r)
print(d)