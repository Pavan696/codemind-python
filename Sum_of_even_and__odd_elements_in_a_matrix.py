a,b = map(int,input().split())
e=0
o=0
for i in range(a):
    x=list(map(int,input().split()))
    for j in x:
        if j%2==0:
            e+=j
        else:
            o+=j
print(e,o)