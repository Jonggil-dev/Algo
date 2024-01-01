'''
설계
1. 각 볼링 공의 무게 별 갯수 기록 하기
2. A가 각 무게별로 하나를 먼저 골랐다고 가정했을 때 B가 고를 수 있는 볼링공의 경우의수 찾기
'''

N, M = map(int, input().split())
nums = list(map(int,input().split()))
ball_ls = [0] * (N+1)
res = 0

for num in nums:
    ball_ls[num] += 1

for balls in ball_ls:
    N -= balls
    res += (balls * N)

print(res)