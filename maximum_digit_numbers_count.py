a=int(input())
l=list(map(int,input().split()))
n=[]
for i in l:
    n.append(len(str(i)))
for i in range(a):
    if n[i]==max(n):
        print(l[i],end=' ')