N,M=map(int,input().split())
num=list(map(int,input().split()))
num.sort()
tmp=[]
def func(st):
    if len(tmp)==M:
        print(*tmp)
        return
    for i in range(st,N):
        if num[i] not in tmp:
            tmp.append(num[i])
            func(i+1)
            tmp.pop()
func(0)