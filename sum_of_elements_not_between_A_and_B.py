n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
sum=0
for i in range(a,b+1):
    c.append(i)
for i in l:
    if i not in c:
        sum+=i
print(sum)