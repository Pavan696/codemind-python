
a,b=map(int,input().split())
c=0
for i in range(a):
    l=list(map(int,input().split()))
    if sorted(l)==l or sorted(l,reverse=True)==l:
        c+=1
print(c)