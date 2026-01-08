import sys
input=sys.stdin.readline

N,X=map(int,input().split())
li=[]
for i in range(N):
    a,b,c,t=map(int,input().split())
    if ((c+a-1)//a)*a<X:
        continue
    st=((X+a-1)//a)*a
    mid=((c+a-1)//a)*a
    end=mid-(mid-X)//b*b
    st_time,mid_time=((X+a-1)//a),((c+a-1)//a)
    end_time=mid_time+(mid-X)//b
    li.append((t+st_time,0))
    li.append((t+end_time,1))
li.sort(key=lambda x:(x[0],x[1]))
res,cnt,before,idx=0,0,0,0
for a,b in li:
    if b==0:
        cnt+=1
    else:
        cnt-=1
    if before<3 and cnt>=3:
        idx=a
    elif before>=3 and cnt<3:
        res+=a-idx+1
    before=cnt
print(res)