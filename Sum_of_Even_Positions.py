n=int(input())
x=list(map(int,input().split()))
cnt=0
for i in range(len(x)):
    if i%2==0:
        cnt+=x[i]
print(cnt)