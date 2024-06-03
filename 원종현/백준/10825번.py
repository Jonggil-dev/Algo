import sys
input=sys.stdin.readline
N=int(input())
li=[]
for i in range(N):
    S,K,E,M=input().rstrip().split()
    K=int(K)
    E=int(E)
    M=int(M)
    li.append((S,K,E,M))
li.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in li:
    print(i[0])