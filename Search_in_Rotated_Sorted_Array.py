a=int(input())
l=list(map(int,input().split()))
b=int(input())
for i in range(a):
    if l[i] == b:
        print(i)
        break
else:
    print('-1')