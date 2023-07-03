a=list(input())
b='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM '
c=0
for i in a:
    if i not in b:
        c+=1
print(c)
