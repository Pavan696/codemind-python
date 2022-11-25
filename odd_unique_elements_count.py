a=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i not in k:
        if i%2!=0:
            k.append(i)
d=len(k)
print(d)