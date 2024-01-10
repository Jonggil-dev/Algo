import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    x1,y1,x2,y2=map(int,input().split())
    li.append([[x1,y1],[x2,y2]])

def on_segment(p, q, r):
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
        q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False

def do_intersect(p1, q1, p2, q2):
    o1 = check(p1, q1, p2)
    o2 = check(p1, q1, q2)
    o3 = check(p2, q2, p1)
    o4 = check(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases - Checking if line segment endpoints lie on the other line segment
    if (o1 == 0 and on_segment(p1, p2, q1)) or (o2 == 0 and on_segment(p1, q2, q1)) or \
       (o3 == 0 and on_segment(p2, p1, q2)) or (o4 == 0 and on_segment(p2, q1, q2)):
        return True

    return False
def check(p1,p2,p3):
    A=p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]
    B=p1[1]*p2[0]+p2[1]*p3[0]+p3[1]*p1[0]
    if A-B>0:
        return 1
    elif A-B<0:
        return -1
    else:
        return 0

def bfs(x):
    global visit,res
    q=deque([])
    q.append(x)
    visit[x]=1
    tmp=1
    while q:
        x=q.popleft()
        for y in graph[x]:
            if not visit[y]:
                visit[y]=1
                tmp+=1
                q.append(y)
    res[1]=max(res[1],tmp)
res={}
res=[0,0]
visit=[0]*(N)
graph=[[] for _ in range(N)]
for i in range(N-1):
    for j in range(i+1,N):
        if do_intersect(li[i][0],li[i][1],li[j][0],li[j][1]):
            graph[i].append(j)
            graph[j].append(i)
for i in range(N):
    if not visit[i]:
        bfs(i)
        res[0]+=1
print(*res,sep="\n")