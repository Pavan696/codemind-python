n=int(input())
x=list(map(int,input().split()))
print(sum(i for i in x if i%2!=0 ))