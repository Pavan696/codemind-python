a=int(input())
s=list(map(int,input().split()))
g=[]
c=0
for i in s:
    if(i<0):
        i=abs(i)
    i=len(list(str(i)))
    g.append(i)
print(*g)