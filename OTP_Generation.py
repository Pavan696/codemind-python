a=input()
b=''
for i in a:
    if int(i)%2!=0:
        c=int(i)**2
        b+=str(c)
print(b)    