a=input()
l=a.split()
k=[]
m=[]
for i in range(len(l)-1,-1,-1):
    k.append(l[i])
for i in k:
    j=i
    g=j[::-1]
    m.append(g)
print(*m)