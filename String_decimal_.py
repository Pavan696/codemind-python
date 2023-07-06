a=int(input())
for i in range(a):
    b=input()
    c='1234567890'
    for i in b:
        if i not in c:
            print(False)
            break
    else:
        print(True)