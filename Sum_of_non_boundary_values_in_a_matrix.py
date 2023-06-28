r,c = map(int,input().split())
l=[]
for i in range(r):
    lst=list(map(int,input().split()))
    l.append(lst)
s=0
for i in range(1,r-1):
    for j in range(1,c-1):
        s+=l[i][j]
print(s)