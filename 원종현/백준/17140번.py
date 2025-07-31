import sys
input=sys.stdin.readline

r,c,k=map(int,input().split())
li=[list(map(int,input().split())) for _ in range(3)]
t=0

def func():
    V=0
    for i in range(len(li)):
        now={}
        tmp=[]
        for j in li[i]:
            if j==0:continue
            if j in now:
                now[j]+=1
            else:
                now[j]=1
        now=[(k,v) for k,v in sorted(now.items(),key=lambda x:(x[1],x[0]))]
        for j in now:
            tmp.extend(j)
        V=max(V,min(len(tmp),100))
        li[i]=tmp[:max(100,len(tmp))]
    for i in li:
        i.extend([0]*(V-len(i)))

while True:
    if len(li)>=r and len(li[0])>=c and li[r-1][c-1]==k:
        break
    if t==101:
        break
    if len(li)>=len(li[0]):
        func()
    else:
        li=[list(i) for i in zip(*li)]
        func()
        li=[list(i) for i in zip(*li)]
    t+=1
print(-1 if t==101 else t)
