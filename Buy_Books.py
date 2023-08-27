a=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
print('0' if (sum(l2)-sum(l1)<0) else sum(l2)-sum(l1))