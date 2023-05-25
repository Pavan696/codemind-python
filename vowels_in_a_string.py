a=input()
l=list(a)
s=input()
v="aeiouAEIOU"
for i in range(len(l)):
    if l[i] == s:
        print('True')
        print(i)
        break
else:
    print('False')