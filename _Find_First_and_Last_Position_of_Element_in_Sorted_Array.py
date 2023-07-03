a=int(input())
l=list(map(int,input().split()))
b=int(input())
c=[]
for i in range(a):
    if l[i]==b:
        c.append(i)
if len(c)>0:
    print(min(c),max(c))
else:
    print('-1 -1')
