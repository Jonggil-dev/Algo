N,M=map(int,input().split())

graph=[[set(),set()]for _ in range(N+1)]
chk=[[set(),set()]for _ in range(N+1)]
res=0
def func(now,flag=0):
    global chk
    if len(chk[now][flag]):
        return
    for j in graph[now][flag]:
        func(j,flag)
        chk[now][flag].add(j)
        chk[now][flag]=chk[now][flag].union(chk[j][flag])

for i in range(M):
    a,b=map(int,input().split())
    graph[b][0].add(a)
    graph[a][1].add(b)

for i in range(1,N+1):
    func(i,0)
    func(i,1)
for i in range(1,N+1):
    if len(chk[i][0])+len(chk[i][1])==N-1:
        res+=1
print(res)