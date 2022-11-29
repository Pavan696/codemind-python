s=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
m=[]
for i in l:
    if a<=i<=b:
        k.append(i)
    else:
        m.append(i)
if len(m)>0:
    print(min(m))
else:
    print(str(-1))