from collections import deque
d=[0,0,1,-1]
li=[input() for _ in range(5)]
loc=[]
for x in range(5):
    for y in range(5):
        if li[x][y]=='*':
            loc.append((x+1,y+1))
size=len(loc)
pos=[]
per=[]
def func(r):
    if len(r)==size:
        pos.append(r)
        return
    for i in range(1+(r[-1] if r else 0),26):
        func(r+[i])
def func2(r,r2):
    if len(r)==size:
        per.append(r)
        return
    for i in range(1,size+1):
        if i not in r2:
            func2(r+[i],r2.union({i}))
def connected(nowloc):
    visit=set()
    locset=set(nowloc)
    q=deque([])
    g=1
    q.append(nowloc[0])
    visit.add(nowloc[0])
    while q:
        c_now=q.popleft()
        for i in range(4):
            nx=c_now[0]+d[i]
            ny=c_now[1]+d[3-i]
            if 1<=nx<=5 and 1<=ny<=5 and (nx,ny) in locset and (nx,ny)not in visit:
                q.append((nx,ny))
                g+=1
                visit.add((nx,ny))
    if g!=size:
        return False
    else:
        return True
def get_total_len(nowper,nowloc):
    tmp_len=0
    c=0
    for i in nowper:
        i-=1
        tmp_len+=abs(loc[i][0]-nowloc[c][0])+abs(loc[i][1]-nowloc[c][1])
        c+=1
    return tmp_len
func([])
func2([],set())
r=10**9
if connected(loc):
    print(0)
else:
    for now_pos in pos:
        nowloc=[]
        for i in now_pos:
            nowloc.append((1+(i-1)//5,(i%5 if i%5 else 5)))

        if not connected(nowloc):
            continue
        tmp=0
        for nowper in per:
            tmp=get_total_len(nowper,nowloc)
            if tmp<r:
                r=tmp
    print(r)
