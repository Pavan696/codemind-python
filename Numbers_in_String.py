a=input()
b='0123456789'
s=0
for i in a:
    if i in b:
        s+=int(i)
print(s)