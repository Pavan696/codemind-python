s=input()
l=s.split()
n=[]
for k in l:
    a=list(k)
    i=0
    j=len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i] 
        i+=1
        j-=1
    n.append(''.join(a))

print(*n)