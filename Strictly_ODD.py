a=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(len(l)):
    if l[i]%2!=0:
        if i%2!=0:
            c+=1
        d+=1
if c==d:
    print('True')
else:
    print('False')