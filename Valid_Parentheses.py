a=int(input())
for i in range(a):
    s=input()
    stack=[]
    c=0
    for i in s:
        if (i=='{' or i=='[' or i=='('):
            stack.append(i)
        if c==1:
            break
        else:
            if i=='}':
                if len(stack)!=0 and stack[-1]=='{':
                    stack.pop()
                else:
                    c=1
            elif i==']':
                if len(stack)!=0 and stack[-1]=='[':
                    stack.pop()
                else:
                    c=1
            elif i==')':
                if len(stack)!=0 and stack[-1]=='(':
                    stack.pop()
                else:
                    c=1
    if len(stack)==0 and c==0:
        print(True)
    else:
        print(False)
            
                