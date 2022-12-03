def rev(a):
    s=0
    while a!=0:
        r=a%10
        s=s*10+r
        a//=10
    return s

a=int(input())
c=rev(a)
if a**2==rev(c**2):
    print(True)
else:
    print(False)