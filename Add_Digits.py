def sum(num):
    sum1=0

    for i in str(num):
        sum1+=int(i)
    if sum1>0 and sum1<10:
        print(sum1)
    else:
       sum(sum1)
    
    
num=int(input())
sum(num)

