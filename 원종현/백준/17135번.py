from itertools import combinations
import sys
input=sys.stdin.readline

def getTarget(enemy,bow):
    tmp=[]
    for k,v in enemy.items():
        length=abs(bow[0]-v[0])+abs(bow[1]-v[1])
        if length<=D:
            tmp.append((k,abs(bow[0]-v[0])+abs(bow[1]-v[1]),v[1]))
    if not tmp:
        return -1
    tmp.sort(key=lambda x:(x[1],x[2]))
    return tmp[0]

N,M,D=map(int,input().split())
li=[list(map(int,input().split())) for i in range(N)]
enemy={}
idx=0
for i in range(N):
    tmp=[]
    for j in range(M):
        if li[i][j]==1:
            enemy[idx]=[i,j]
            idx+=1
        else:
            tmp.append([i,j])

total_enemy=len(enemy)
res=0
for j in combinations([[N,i] for i in range(M)],3):
    tmp_enemy={k:v for k,v in enemy.items()}
    tmp_res=0
    while tmp_enemy:
        targets=set()
        for bow in j:
            v=getTarget(tmp_enemy,bow)
            if v!=-1:
                targets.add(v[0])
        for i in targets:
            tmp_res+=1
            del tmp_enemy[i]
        k=[*tmp_enemy.keys()]
        for i in k:
            x,y=tmp_enemy[i]
            if x+1==N:
                del tmp_enemy[i]
            else:
                tmp_enemy[i]=[x+1,y]
    res=max(res,tmp_res)

print(res)