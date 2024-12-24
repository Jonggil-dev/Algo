import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
N=int(input())
li=list(map(int,input().split()))
S=int(input())
res=1
visit=[0]*N
def func(x):
    global res
    for i in (x-li[x],x+li[x]):
        if 0<=i<N and not visit[i]:
            res+=1
            visit[i]=1
            func(i)
func(S-1)
print(res)