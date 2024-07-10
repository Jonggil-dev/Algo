import sys
input=sys.stdin.readline

N=int(input())
x_sum=[0]*(N+1)
y_sum=[0]*(N+1)
dp=[0]*(N+1)
sx=[] # 크기순으로 정렬된 x
sy=[] # 크기순으로 정렬된 y
res=[float('inf'),0]

for i in range(1,N+1):
    nx,ny=map(int,input().split())
    sx.append((nx,i))
    sy.append((ny,i))
sx.sort()
sy.sort()
sx=[0]+sx
sy=[0]+sy

for i in range(1,N+1):
    x_sum[i]+=x_sum[i-1]+sx[i][0]
    y_sum[i]+=y_sum[i-1]+sy[i][0]


for i in range(1,N+1):
    left_x=((i-1)*(sx[i][0])-x_sum[i-1]) #(현재x*(i-1))-(1번부터 i-1번까지의 합)
    right_x=((x_sum[N]-x_sum[i])-(N-i)*sx[i][0]) # i+1~N까지합 - (N-i)*현재x
    left_y=((i-1)*(sy[i][0])-y_sum[i-1])
    right_y=((y_sum[N]-y_sum[i])-(N-i)*sy[i][0])

    dp[sx[i][1]]+=left_x+right_x
    dp[sy[i][1]]+=left_y+right_y

for i in range(1,N+1):
    if dp[i]<res[0]:
        res=[dp[i],i]
print(res[1])
