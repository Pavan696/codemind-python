a=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i < 0:
        i=abs(i)
    i=len(str(i))
    b.append(i)
for i in range(a):
    if b[i]==max(b):
        print(l[i],end=' ')