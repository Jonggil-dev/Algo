import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
N,S=map(int,input().split())
res=10**9
w=[0]+list(map(int,input().split()))
t=[0]+list(map(int,input().split()))
p=[0]+list(map(int,input().split()))
graph=[[] for _ in range(N+1)]
dic={}
for i in range(1,N+1):
    graph[p[i]].append(i)

def func(now,time,work,parent):
    if parent!=0:
        if parent in dic:
            dic[parent].append(now)
        else:
            dic[parent]=[now]
    w[now]+=work
    t[now]+=time
    for i in graph[now]:
        func(i,t[now],w[now],i if parent==0 else parent)

func(0,0,0,0)
#print(graph)
#print(dic)
#print(w)
#print(t)
#print(p)

dp={}
for _,jobs in dic.items():
    tmp={}
    for job in jobs:
        for work,time in dp.items():
            cost=work+w[job]
            if cost<S:
                if cost in tmp:
                    tmp[cost]=min(time+t[job],tmp[cost])
                else:
                    tmp[cost]=time+t[job]
            else:
                res=min(res,time+t[job])
        if w[job]<S:
            if w[job] in tmp:
                tmp[w[job]]=min(tmp[w[job]],t[job])
            else:
                tmp[w[job]]=t[job]
        else:
            res=min(res,t[job])
    for work,time in tmp.items():
        if work in dp:
            dp[work]=min(dp[work],tmp[work])
        else:
            dp[work]=tmp[work]
#print(dp)
print(res if res!=10**9 else -1)