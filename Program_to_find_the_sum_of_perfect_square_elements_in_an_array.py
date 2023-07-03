def is_per(i):
    j=int(i**0.5)
    if j*j == i:
        return True
    else:
        return False
a=int(input())
l=list(map(int,input().split()))
b=0
for i in l:
    if is_per(i):
        b+=i
print(b)

    