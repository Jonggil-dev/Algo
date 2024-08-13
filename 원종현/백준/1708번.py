import sys
input=sys.stdin.readline

def ccw(p,q,r):
    return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
N=int(input())
li=[]
for i in range(N):
    x,y=map(int,input().split())
    li.append((x,y))
li.sort(key=lambda x:(x[0],x[1]))
def scan(points):
    tmp=[]
    for r in points:
        while len(tmp)>=2:
            p,q=tmp[-2],tmp[-1]
            if ccw(p,q,r)>0:
                break
            tmp.pop()
        tmp.append(r)
    return tmp
res=set(scan(li)).union(set(scan(li[::-1])))
print(len(res))
