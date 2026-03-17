from bisect import bisect_left, bisect_right,insort
import sys
input=sys.stdin.readline

N,Q=map(int,input().split())
A=list(map(int,input().split()))

blocks=[]
b_size=int(N**0.5)+1
for i in range(0,N,b_size):
    blocks.append(sorted(A[i:i+b_size]))
coords=sorted(list(set(A)))


for _ in range(Q):
    tmp=list(map(int,input().split()))
    if tmp[0]==1:
        i,j,k=map(lambda x:int(x)-1,tmp[1:])
        k+=1
        le,ri=0,len(coords)-1
        res=coords[-1]
        while le<=ri:
            mid=(le+ri)//2
            mv=coords[mid]
            cnt=0
            bl,br=i//b_size,j//b_size

            if bl==br:
                for idx in range(i,j+1):
                    if A[idx]<=mv:
                        cnt+=1
            else:
                for idx in range(i,(bl+1)*b_size):
                    if A[idx]<=mv:
                        cnt+=1
                for b_idx in range(bl+1,br):
                    cnt+=bisect_right(blocks[b_idx],mv)
                for idx in range(br*b_size,j+1):
                    if A[idx]<=mv:
                        cnt+=1
            if cnt>=k:
                res=mv
                ri=mid-1
            else:
                le=mid+1
        print(res)
    else:
        i,j=map(lambda x:int(x)-1,tmp[1:])
        if i==j:
            continue
        b1,b2=i//b_size,j//b_size
        blocks[b1].pop(bisect_left(blocks[b1],A[i]))
        insort(blocks[b1],A[j])
        blocks[b2].pop(bisect_left(blocks[b2],A[j]))
        insort(blocks[b2],A[i])

        A[i],A[j]=A[j],A[i]
