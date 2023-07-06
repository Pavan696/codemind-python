s=input()
l=[]
for i in s:
    l.append(s.count(i))
for i in l:
    if i ==1:
        print(l.index(i))
        break
else:
    print('-1')