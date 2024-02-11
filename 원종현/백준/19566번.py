from collections import defaultdict
N,K=map(int,input().split())
li=[0]+list(map(int,input().split()))
r=0
dic=defaultdict(int)
for i in range(1,N+1):
    li[i]+=li[i-1]
    c=li[i]-K*i
    r+=dic[c]
    dic[c]+=1

print(r+dic[0])