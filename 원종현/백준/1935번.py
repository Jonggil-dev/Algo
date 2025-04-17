N=int(input())
S=input()
li=[int(input()) for _ in range(N)]

stk=[]
for i in S:
    if i.isalpha():
        stk.append(li[ord(i)-ord('A')])
    else:
        t1,t2=float(stk.pop()),float(stk.pop())
        if i=='+':
            stk.append(t2+t1)
        elif i=='-':
            stk.append(t2-t1)
        elif i=='*':
            stk.append(t2*t1)
        elif i=='/':
            stk.append(t2/t1)
print('%.2f'%stk[0])