res=1
while True:
    stk=[]
    cnt=0
    S=input()
    if '-' in S:
        break
    for i in S:
        if i=="{":
            stk.append(i)
        else:
            if stk:
                stk.pop()
            else:
                cnt+=1
                stk.append('{')
    cnt+=len(stk)//2
    print(f'{res}. {cnt}')
    res+=1