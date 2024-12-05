N,M=map(int,input().split())
li=sorted(list(map(int,input().split())))
tmp=[]

def func():
    if len(tmp)==M:
        print(*tmp)
        return
    r=0
    for i in range(N):
        if r!=li[i]:
            tmp.append(li[i])
            r=li[i]
            func()
            tmp.pop()

func()