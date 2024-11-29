import sys
input=sys.stdin.readline
K,L=map(int,input().split())
dic={}
for i in range(L):
    dic[input().rstrip()]=i

res=sorted(dic.items(), key=lambda x:x[1])
K=min(K,len(res))
for i in range(K):
    print(res[i][0])