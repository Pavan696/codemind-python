a=int(input())
l=list(map(int,input().split()))
sum1=0
sum2=0
for i in range(0,a//2+1):
      sum1+=i
for j in range(a//2+1,a+1):
    sum2+=j
print(abs(sum1-sum2))
