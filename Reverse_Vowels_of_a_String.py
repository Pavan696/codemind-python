s=input()
l=list(s)
i=0
j=len(s)-1
k=['a','e','i','o','u','A','E','I','O','U']
while i < j:
    if l[i] not in k: 
        i+=1
    elif l[j] not in k:
        j-=1
    else:
        l[i],l[j]=l[j],l[i]
        i+=1
        j-=1
print(''.join(l))