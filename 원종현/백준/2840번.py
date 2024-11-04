from collections import deque
N,K=map(int,input().split())
q=deque(['?']*N)
for i in range(K):
    s,c=input().split()
    s=int(s)%N
    for _ in range(s):
        q.appendleft(q.pop())
    if q[0]=='?':
        if c in q:
            print('!')
            break
        q[0]=c
    elif q[0]==c:
        continue
    else:
        print('!')
        break
else:
    print(''.join(q))