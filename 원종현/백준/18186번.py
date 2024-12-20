import sys
input=sys.stdin.readline
N,B,C=map(int,input().split())
li=[0]+list(map(int,input().split()))+[0,0]
res=0

def buythree(idx):
    global res
    k=min(li[idx:idx+3])
    for j in range(idx,idx+3):
        li[j]-=k
    res+=(B+2*C)*k

def buytwo(idx,type=0):
    global res
    if type:
        k=min(li[idx],li[idx+1]-li[idx+2])
    else:
        k=min(li[idx:idx+2])
    for j in range(idx,idx+2):
        li[j]-=k
    res+=(B+C)*k

def buyone(idx):
    global res
    res+=B*li[idx]
    li[idx]=0

for i in range(1,N+1):
    if li[i]:
        if B>C:
            if li[i+1]>li[i+2]:
                buytwo(i,1)
                buythree(i)
            else:
                buythree(i)
                buytwo(i)
        buyone(i)
print(res)