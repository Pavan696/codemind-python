s=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
for i in l:
    if a<=i<=b:
        k.append(i)
if len(k)>0:
    print(max(k))
else:
    print(str(-1))