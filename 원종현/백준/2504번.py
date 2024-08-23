li=input()
stk=[]
res=0
tmp=1
for i in range(len(li)):
    if li[i]=='(':
        stk.append(li[i])
        tmp*=2
    elif li[i]=='[':
        stk.append(li[i])
        tmp*=3
    elif li[i]==')':
        if not stk or stk[-1]=='[':
            res=0
            break
        if li[i-1]=='(':
            res+=tmp
        stk.pop()
        tmp//=2
    else:
        if not stk or stk[-1]=='(':
            res=0
            break
        if li[i-1]=='[':
            res+=tmp
        stk.pop()
        tmp//=3
print(0 if stk else res)