a=int(input())
l=list(map(int,input().split()))
if a%2!=0:
    l.append(0)
print(*l)