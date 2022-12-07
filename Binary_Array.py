a=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if i!=0 and i!=1:
        c.append(i)
if len(c)==0:
    print('True')
else:
    print('False')