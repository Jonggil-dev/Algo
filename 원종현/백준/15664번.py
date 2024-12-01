N,M=map(int,input().split())
li=sorted(list(map(int,input().split())))
visit=[0]*N
tmp=[]
def func(idx):
    if len(tmp)==M:
        print(*tmp)
        return
    d=0
    for i in range(idx,N):
        if not visit[i] and d!=li[i]:
            visit[i]=1
            tmp.append(li[i])
            d=li[i]
            func(i+1)
            visit[i]=0
            tmp.pop()
func(0)