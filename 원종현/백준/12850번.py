N=int(input())
graph=[[1,2],[0,2,3],[0,1,3,4],[1,2,4,5],[2,3,5,6],[5,6],[4,7]]
MOD = 1000000007
graph1=[
        [0, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0]
]
def mul(g1,g2):
    return [[sum(g1[i][k]*g2[k][j]%MOD for k in range(8))%MOD for j in range(8)] for i in range(8)]

graph2=[[0]*8 for _ in range(8)]
for i in range(8):graph2[i][i]=1
while N>0:
    if N%2!=0:
        graph2=mul(graph1,graph2)
        N-=1
    graph1=mul(graph1,graph1)
    N//=2
print(graph2[0][0])