a=int(input())
l=list(map(int,input().split()))
b,c=map(int,input().split())
k=[]
for i in l:
    if b<=i<=c:
         k.append(i)
if len(k)>0:
    print(*k)
else:
    print(str(-1))