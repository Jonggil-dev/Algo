A,B,N=map(int,input().split())
li=[]
for i in range(N):
    A=(A-(A//B)*B)*10
    li.append(A//B)
print(li[N-1])