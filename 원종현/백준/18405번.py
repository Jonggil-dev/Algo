import sys
input=sys.stdin.readline
dir=[0,0,1,-1]
N,k=map(int,input().split())
li=[[]]
d={}
check=set()
for i in range(N):
    tmp=[0]+list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j]:
            check.add(tmp[j])
            if tmp[j] not in d:
                d[tmp[j]]={(i+1,j)}
            else:
                d[tmp[j]].add((i+1,j))
    li.append(tmp)
check=sorted(list(check))
S,X,Y=map(int,input().split())
cnt=0
while cnt<S:
    for i in check:
        del_tmp=[]
        add_tmp=[]
        for x,y in d[i]:
            for s in range(4):
                nx,ny=x+dir[s],y+dir[3-s]
                if 1<=nx<=N and 1<=ny<=N and not li[nx][ny]:
                    li[nx][ny]=i
                    add_tmp.append((nx,ny,i))
            del_tmp.append((x,y))
        for x,y in del_tmp:
            d[i].remove((x,y))
        for x,y,p in add_tmp:
            d[p].add((x,y))
    cnt+=1
print(li[X][Y])