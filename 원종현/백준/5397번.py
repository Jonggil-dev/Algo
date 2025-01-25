for _ in range(int(input())):
    lli=[]
    rli=[]
    data=input()
    for i in data:
        if i=='-':
            if lli:
                lli.pop()
        elif i=='<':
            if lli:
                rli.append(lli.pop())
        elif i=='>':
            if rli:
                lli.append(rli.pop())
        else:
            lli.append(i)
    lli.extend(reversed(rli))
    print(''.join(lli))