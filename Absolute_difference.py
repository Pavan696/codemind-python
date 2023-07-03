def prime(i):
    if i==1:
        return 0
    elif i==2:
        return 1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return 0
            break
    return 1
a=int(input())
l=list(map(int,input().split()))
c,d=1,1
for i in l:
    if prime(i):
        c*=i
    else:
        d*=i
print(abs(c-d))