import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def func(x):
    if visit[x]==idx:
        return 0
    visit[x]=idx
    for i in li[x]:
        if check[i]==-1 or func(check[i]):
            check[i]=x
            return 1
    return 0

for _ in range(int(input())):
    c,d,v=map(int,input().split())
    li={}
    A,B=[],[]
    for i in range(v):
        a,b=input().rstrip().split()
        if a[0]=='C':A.append((i,a,b))
        if a[0]=='D':
            B.append((i,b,a))
            li[i]=[]
    for i,a,b in A:
        for j,c,d in B:
            if a==c or b==d:
                li[j].append(i)
    check=[-1]*v
    visit=[0]*v
    idx=1
    for i in li.keys():
        func(i)
        idx+=1
    print(v-sum([1 for i in check if i!=-1]))