from itertools import combinations
S=list(input())

def func(idx):
    tmp=S[:]
    for x,y in idx:
        tmp[x]=''
        tmp[y]=''
    return ''.join(tmp)
idx=[]
stk=[]

for i in range(len(S)):
    if S[i]=='(':
        stk.append(i)
    elif S[i]==')':
        idx.append((stk.pop(),i))

res=set()
for i in range(1,len(idx)+1):
    for j in combinations(idx,i):
        res.add(func(j))
res=sorted(list(res))
for i in res:
    print(i)