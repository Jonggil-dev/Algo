def func(st,end,now):
    if st==end:
        res[now].append(tree[st])
        return
    mid=(st+end)//2
    res[now].append(tree[mid])
    func(st,mid-1,now+1)
    func(mid+1,end,now+1)

K=int(input())
tree=list(map(int,input().split()))
res=[[] for _ in range(K)]
func(0,len(tree)-1,0)
for i in res:
    print(*i)