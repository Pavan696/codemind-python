def rev(x):
    c=0
    while x!=0:
        r=x%10
        c=c*10+r
        x//=10
    return c
a=int(input())
c=rev(a)
if a**2 == rev(c**2):
    print(True)
else:
    print(False)