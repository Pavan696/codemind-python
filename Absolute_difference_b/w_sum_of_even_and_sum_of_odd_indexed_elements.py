a=int(input())
l=list(map(int,input().split()))
oc=0
ec=0
for i in range(len(l)):
    if i%2==0:
        oc+=l[i]
    else:
        ec+=l[i]
print(abs(ec-oc))
