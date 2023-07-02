a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    b1=list(map(int,input().split()))
    c1=list(map(int,input().split()))
    d=[]
    for i in range(b):
        d.append(b1[i])
    for i in range(c):
        d.append(c1[i])
    print(*sorted(d))