n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
for i in l:
    if i==1:
        c+=1
        a.append(c)
    else:
        c=0
        a.append(c)
print(max(a))