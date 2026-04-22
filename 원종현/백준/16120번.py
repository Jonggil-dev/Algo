S=input()
stk=[]
for i in range(len(S)):
    stk.append(S[i])
    while len(stk)>=4 and ''.join(stk[-4:])=='PPAP':
        for _ in range(3):
            stk.pop()

print('PPAP' if ''.join(stk)=='P' else 'NP')