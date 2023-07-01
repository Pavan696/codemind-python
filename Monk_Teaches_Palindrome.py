a=int(input())
for i in range(a):
    b=input()
    c=b[::-1]
    if c==b and len(b)%2==0:
        print('YES EVEN')
    elif c==b and len(b)%2!=0:
        print('YES ODD')
    else:
        print('NO')