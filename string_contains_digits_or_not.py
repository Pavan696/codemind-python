a=int(input())
for i in range(a):
    s=input()
    for i in s:
        if i>='0' and i<='9':
            print('Yes')
            break
    else:
        print('No')