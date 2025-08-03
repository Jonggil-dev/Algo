import sys
input=sys.stdin.readline

N,K=map(int,input().split())
li=[]
res=0

for i in range(N):
    li.append(list(map(int,input().split())))
li.sort(key=lambda x:x[1])
st,end,t=0,0,0
while st<=end and end<N:
    if li[end][1]-li[st][1]<=2*K:
        t+=li[end][0]
        res=max(res,t)
        end+=1
    else:
        t-=li[st][0]
        st+=1
print(res)