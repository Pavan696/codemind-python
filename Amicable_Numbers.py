a=int(input())
b=int(input())
c=0
for i in range(1,a):
    if(a%i==0):
        c+=i
k=0
for j in range(1,b):
    if(b%j==0):
        k+=j
if (k==a)and(c==b):
    print("Amicable")
else:
    print("Not Amicable")