import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def func(x):
    if visit[x]:
        return 0
    visit[x]=1
    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0

N,M,K=map(int,input().split())
li={}
people=[]
for i in range(K):
    n,m,c=map(int,input().split())
    people.append((n,m,c))
    if c!=0:
        li[i]=[]

for i in range(K):
    if people[i][2]==1:
        continue
    for j in range(K):
        if i==j or people[j][2]==0:
            continue
        if people[i][0]==people[j][0] or people[i][1]==people[j][1]:
            li[j].append(i)

check=[-1]*K
for i in li.keys():
    visit=[0]*K
    func(i)

print(sum([1 for i in check if i!=-1]))