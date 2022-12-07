import math
def prime(x):
    if x==0 or x==1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
    return True
a=int(input())
c=[]
b=[]
for i in range(1,a+1):
    if a%i==0:
        b.append(i)
for i in b:
    if prime(i)!=True:
        c.append(i)
print(len(c))