a=list(input())
u,d,l,r = 0,0,0,0
for i in a:
    if i == 'U':
        u+=1
    elif i == 'D':
        d-=1
    elif i == 'L':
        l-=1
    elif i == 'R':
        r+=1
s=u+d+l+r
if s==0:
    print('True')
else:
    print('False')