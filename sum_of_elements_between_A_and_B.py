a=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=0
for i in l:
    if a<= i <=b:
         k+=i
print(k)
