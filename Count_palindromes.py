def palndrm(x):
    sum=0
    t=x
    while x!=0:
        rem=x%10
        sum=sum*10+rem
        x//=10
    if sum==t:
        return True
    return False
a=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if palndrm(i)==True:
        c+=1
print(c)    
    