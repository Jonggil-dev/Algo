N,d=map(int,input().split())
li=list(map(int,input().split()))
res=[(-d+1,-1),(float('inf'),N)]
cand=[]
def find(x):
    idx=0
    for i in range(len(res)):
        if res[i][0]>li[x]:
            idx=i
            break
    st,end=idx-1,idx
    if res[st][0]+d<=li[x]<=res[end][0]-d:
        res.append((li[x],x))
    else:
        for i in cand:
            if i>=li[x]:
                res.append((i,x))
                break

def update():
    global cand
    cand=[]
    for i in range(len(res)-1):
        if i==0 and res[i+1][0]-d>0:
            cand.append(1)
            continue
        if res[i+1][0]-res[i][0]>=d*2:
            cand.append(res[i][0]+d)
            continue


for i in range(N):
    find(i)
    res.sort(key=lambda x:x[0])
    update()

print(*[i[0] for i in sorted(res[1:-1],key=lambda x:x[1])])