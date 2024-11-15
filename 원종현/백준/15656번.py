N,M=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
def func(now,idx):
    if idx==M-1:
        print(*now)
        return
    for i in range(N):
        func(now+[li[i]],idx+1)
func([],-1)
