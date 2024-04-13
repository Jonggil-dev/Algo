from collections import deque
N,K=map(int,input().split())
M=len(str(N))

visit=set()
visit.add((N,0))
q=deque()
q.append((N,0))
r=0
while q:
    n,k=q.popleft()
    if k==K:
        r=max(r,n)
        continue
    li=list(str(n))
    for i in range(M-1):
        for j in range(i+1,M):
            if i==0 and li[j]=='0':
                continue
            li[i],li[j]=li[j],li[i]
            re=int(''.join(li))
            if (re,k+1) not in visit:
                q.append((re,k+1))
                visit.add((re,k+1))
            li[i],li[j]=li[j],li[i]
print(r if r else -1)