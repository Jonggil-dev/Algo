from collections import deque
N=int(input())
li=[input() for _ in range(N)]

def func(a,b):
    if len(a)!=len(b):
        return b
    qb=deque(b)
    for _ in range(len(a)):
        qb.rotate(1)
        t=''.join(qb)
        if t==a: return t
    return ''.join(qb)

for i in range(N):
    for j in range(i+1,N):
        if li[i]!=li[j]:
            li[j]=func(li[i],li[j])
print(len(set(li)))