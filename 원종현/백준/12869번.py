from itertools import permutations
N=int(input())
li=list(map(int,input().split()))
for i in range(3-len(li)):
    li.append(0)
de=[i for i in permutations([9,3,1],3)]
res=10**9
print(de)
d={}
def func(now,cnt):
    global res
    if sum(now)==0:
        res=min(res,cnt)
        return
    for a,b,c in de:
        next=sorted([max(0,now[0]-a),max(0,now[1]-b),max(0,now[2]-c)])
        n_str=','.join([str(i) for i in next])
        if n_str in d and d[n_str]>cnt+1:
            d[n_str]=cnt+1
            func(next,cnt+1)
        elif n_str not in d:
            d[n_str]=cnt+1
            func(next,cnt+1)

func(li,0)
print(res)
