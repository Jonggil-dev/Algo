d=[0,0,1,-1]
N=int(input())
li=[]
T,S=set(),set()
for i in range(N):
    tmp=input().split()
    for j in range(N):
        if tmp[j]=='T':
            T.add((i,j))
        if tmp[j]=='S':
            S.add((i,j))
    li.append(tmp)

def check(well):
    cnt=1
    for tx,ty in T:
        if not cnt:
            break
        for idx in range(4):
            nx,ny=tx+d[idx],ty+d[3-idx]
            while 0<=nx<N and 0<=ny<N:
                if (nx,ny) in S:
                    cnt=0
                    break
                if (nx,ny) in well or (nx,ny) in T:
                    break
                nx+=d[idx]
                ny+=d[3-idx]
    return cnt
res=0
for i in range(N*N):
    if (i//N,i%N)in S or (i//N,i%N)in T or res:
        continue
    for j in range(i+1,N*N):
        if (j//N,j%N)in S or (j//N,j%N)in T or res:
            continue
        for k in range(j+1,N*N):
            if (k//N,k%N)in S or (k//N,k%N)in T or res:
                continue
            well=set([(i//N,i%N),(j//N,j%N),(k//N,k%N)])
            if check(well):
                res=1
                break
print("YES" if res else "NO")