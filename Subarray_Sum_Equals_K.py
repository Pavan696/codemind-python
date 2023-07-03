a,b=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    if i == b:
        c+=1
for i in range(a):
    s=0
    s+=l[i]
    for j in range(i+1,a):
        s+=l[j]
        if s==b:
            c+=1
        elif s>b:
            break
print(c)