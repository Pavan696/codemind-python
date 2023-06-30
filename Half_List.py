a=int(input())
l=list(map(int,input().split()))
for i in range(a-1,-1,-1):
    print(l[i],end=" ")
    if i <= a//2:
        break
for i in range(a):
    print(l[i],end=" ")
    if i >= (a//2)-1:
        break