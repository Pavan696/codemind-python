a=input().split()
l=[]
for i in a:
    b=list(i)
    c=0
    for j in b:
        if j in 'aeiou':
            c+=1
    l.append(c)
print(max(l))