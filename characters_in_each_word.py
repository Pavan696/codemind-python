a=str(input())
a=a.split()
l=[]
for i in a:
    l.append(len(i))
print(*l)