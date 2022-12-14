def palndrm(x):
    sum=0
    t=x
    while x!=0:
        rem=x%10
        sum=sum+rem
        x//=10
    return sum
a=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    c.append(palndrm(i))
print(sum(c))  