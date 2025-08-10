stk=[]
res=0
s=input()
for i in s:
    if i not in '+-*/':
        stk.append(int(i))
        continue
    else:
        a=stk.pop()
        b=stk.pop()
    if i=='+':stk.append(a+b)
    elif i=='-':stk.append(b-a)
    elif i=='*':stk.append(a*b)
    elif i=='/':stk.append(b//a)
    else:stk.append(int(i))
print(stk[0])