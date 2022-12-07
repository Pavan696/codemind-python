a=int(input())
l=list(map(int,input().split()))
k=0
c=0
for i in range(len(l)):
    if i%2==0:
        k+=l[i]
    else:
        c+=l[i]
if c==k:
    print('YES')
else:
    print('NO')