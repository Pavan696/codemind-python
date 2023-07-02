a=int(input())
for i in range(a):
    b=int(input())
    l=list(map(int,input().split()))
    c=0
    for k in l:
        for j in l:
            if k!=j:
                if k+j in l:
                    c+=1
                
    print(c//2 if c!=0 else '-1')