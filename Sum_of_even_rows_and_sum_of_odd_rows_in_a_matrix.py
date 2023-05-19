a,b = map(int,input().split())
e=0
o=0
for i in range(a):
    x=list(map(int,input().split()))
    if i%2 == 0:
        e+=sum(x)
    else:
        o+=sum(x)
print(e,o)