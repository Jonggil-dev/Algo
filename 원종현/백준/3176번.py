N=int(input())
li=list(map(int,input().split()))
tree=[[] for _ in range(N)]
for i in range(1,N):
    tree[li[i]].append(i)

r=0
def func(x):
    t=[]
    for i in tree[x]:
        n=func(i)
        t.append(n)
    if t:
        t.sort(reverse=True)
        t=[i+t[i] for i in range(len(t))]
        t.sort()
        return t[-1]+1
    return 0
print(func(0))