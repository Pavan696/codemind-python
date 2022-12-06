a=input()
l=a.split()
k=[]
for i in range(len(l)):
    if i%2==0:
        j=l[i]
        g=j[::-1]
        k.append(g)
    else:
        k.append(l[i])
print(*k)