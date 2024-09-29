N,M=map(int,input().split())
li=[]
for i in range(N):
    li.append(input())
d={'A':0,'C':1,'G':2,'T':3}
cnt=0
res=''
for i in range(M):
    tmp=[0,0,0,0]
    for j in range(N):
        tmp[d[li[j][i]]]+=1
    idx=tmp.index(max(tmp))
    if idx==0:
        res+='A'
    elif idx==1:
        res+='C'
    elif idx==2:
        res+='G'
    elif idx==3:
        res+='T'
    cnt+=N-max(tmp)
print(res)
print(cnt)