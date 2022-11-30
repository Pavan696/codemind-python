a=int(input())
c=0
d=0
while a!=0:
    r=a%10
    a//=10
    if r%2==0:
        c+=1
    else:
        d+=1
if c==0 :
    print('Odd')
elif d==0:
    print('Even')
else:
    print('Mixed')