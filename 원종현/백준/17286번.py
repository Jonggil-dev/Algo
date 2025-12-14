from itertools import permutations

res=10**9
X,Y=[],[]
for _ in range(4):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

for i in permutations([1,2,3],3):
    now=[X[0],Y[0]]
    tmp=0
    for j in i:
        tmp+=(abs(now[0]-X[j])**2+abs(now[1]-Y[j])**2)**0.5
        now=[X[j],Y[j]]
    res=min(res,int(tmp))
print(res)