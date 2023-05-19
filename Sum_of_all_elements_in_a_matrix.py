a,b = map(int,input().split())
o=0
for i in range(a):
    x=list(map(int,input().split()))
    o+=sum(x)
print(o)