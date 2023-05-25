s=input()
v="aeiou"
b=[]
for i in s:
    if i in v and i not in b:
        b.append(i)
if len(b)== len(v):
    print('True')
else:
    print('False')