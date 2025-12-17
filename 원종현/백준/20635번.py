import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
def func(x,y):
    global tmp
    if (x,y) in visit:
        return
    tmp+=1
    visit[(x,y)]=1
    for dy in lix[x]:
        func(x,dy)
    for dx in liy[y]:
        func(dx,y)

def func2(x):
    if visit[x]:
        return 0
    visit[x]=1
    if x in liy:
        for i in liy[x]:
            if check[i]==-1 or func2(check[i]):
                check[i]=x
                return 1
    return 0
N,M=map(int,input().split())
Y=set()
min_res,max_res=10**9,0
lix,liy={},{}
alldots=[]
for i in range(M):
    a,b=map(int,input().split())
    Y.add(b)
    alldots.append((a,b))
    if a in lix:
        lix[a].append(b)
    else:
        lix[a]=[b]
    if b in liy:
        liy[b].append(a)
    else:
        liy[b]=[a]


visit={}
for x,y in alldots:
    tmp=0
    func(x,y)
    if tmp>=2:
        max_res+=tmp-1

check=[-1]*(N+1)
for i in Y:
    visit=[0]*(N+1)
    func2(i)
print(M-sum([1 for i in check if i!=-1]))
print(max_res)

