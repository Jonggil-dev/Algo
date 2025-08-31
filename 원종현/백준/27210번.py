N=int(input())
li=list(map(int,input().split()))
cnt,res=0,0
min_v,max_v=0,0

for i in li:
    if i==1:
        cnt+=1
    elif i==2:
        cnt-=1
    res=max(res,abs(cnt-min_v),abs(max_v-cnt))
    min_v=min(min_v,cnt)
    max_v=max(max_v,cnt)
print(res)