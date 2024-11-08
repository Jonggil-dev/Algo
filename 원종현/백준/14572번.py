import sys
input=sys.stdin.readline
def calc(t,c,lens):
    return (len(t)-len(c))*lens
N,K,D=map(int,input().split())
people=[]
problem={}
for i in range(N):
    M,d=map(int,input().split())
    people.append((M,d,i))
    problem[i]=list(map(int,input().split()))
people.sort(key=lambda x:x[1])
res=0
st,end=0,0
algo=[0]*(31)
now_len=1

while st<=end and end<N:
    if people[end][1]-people[st][1]<=D:
        for i in problem[people[end][2]]:
            algo[i]+=1
        t,c=0,0
        for i in algo:
            if i:
                t+=1
            if i==end-st+1:
                c+=1
        res=max(res,(t-c)*(end-st+1))
        end+=1
    else:
        for i in problem[people[st][2]]:
            algo[i]-=1
        st+=1
print(res)
