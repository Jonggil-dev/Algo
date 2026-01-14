from collections import deque
def dec(idx):
    global cnt,q1
    if q1[idx][1]==1:
        cnt+=1
    q1[idx][1]-=1

N,K=map(int,input().split())
li=list(map(int,input().split()))
q1=deque([[0,i] for i in li[:N]])
q2=deque(li[N:])
res=0
cnt=0
while cnt<K:
    res+=1
    c,a=q1.pop()
    q2.appendleft(a)
    a=q2.pop()
    q1.appendleft([0,a])
    if q1[-1][0] and q1[-1][1]:
        q1[-1][0]=0
    for i in range(N-2,-1,-1):
        if q1[i+1][0]==0 and q1[i+1][1]!=0 and q1[i][0]:
            dec(i+1)
            q1[i][0]=0
            if i+1!=N-1:
                q1[i+1][0]=1
    if q1[0][1]!=0:
        dec(0)
        q1[0][0]=1
print(res)