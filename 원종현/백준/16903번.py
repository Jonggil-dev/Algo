import sys
input=sys.stdin.readline

d={}

def update(x):
    d_tmp=d
    for i in range(29,-1,-1):
        tmp=1 if x&(1<<i) else 0
        #print(x,tmp)
        if tmp not in d_tmp:
            d_tmp[tmp]={2:1}
        else:
            d_tmp[tmp][2]+=1
        d_tmp=d_tmp[tmp]

def delete(x):
    d_tmp=d
    for i in range(29,-1,-1):
        tmp=1 if x&(1<<i) else 0
        d_tmp[tmp][2]-=1
        if not d_tmp[tmp][2]:
            del d_tmp[tmp]
            return
        d_tmp=d_tmp[tmp]

def query(x):
    d_tmp=d
    res=0
    for i in range(29,-1,-1):
        tmp=x&(1<<i)
        corv=[0,1] if x&(1<<i) else [1,0]
        for j in corv:
            if j in d_tmp:
                break
        if j and not tmp or not j and tmp:
            res+=1<<i
        d_tmp=d_tmp[j]
    print(res)

M=int(input())
update(0)

for _ in range(M):
    q,x=map(int,input().split())
    if q==1:
        update(x)
    elif q==2:
        delete(x)
    else:
        query(x)