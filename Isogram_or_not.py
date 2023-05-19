a=input()
l=list(a)
for i in l:
    if l.count(i) > 1:
        print(False)
        break
else:
    print(True)