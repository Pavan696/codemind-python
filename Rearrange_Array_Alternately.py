a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split()))
    i=0
    j=b-1
    d=[]
    while i<=j:
        if i==j:
            d.append(c[i])
        else:
            d.append(c[j])
            d.append(c[i])
        i+=1
        j-=1
    print(*d)