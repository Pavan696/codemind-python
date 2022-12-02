for i in range(int(input())):
    a,b=map(int,input().split())
    ans=-1
    for i in range(b):
        if (i*i)%b==a:
            ans=i
            break
    print(ans)