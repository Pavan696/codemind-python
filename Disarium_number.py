a=input()
b=int(a[::-1])
i=1
sum=0
while b:
    sum+=(b%10)**i
    b//=10
    i+=1
if int(a)==sum:
    print(True)
else:
    print(False)