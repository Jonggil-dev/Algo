N,M,K=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(M)]
tmp=[0]*(N)
res=0

def func(a,idx):
    global res
    if idx==N:
        now=set(tmp)
        cnt=0
        for i in li:
            for j in i:
                if j not in now:
                    break
            else:
                cnt+=1
        if cnt>res:
            res=cnt
        return
    for i in range(a+1,2*N+1):
        tmp[idx]=i
        func(i,idx+1)
func(0,0)
print(res)