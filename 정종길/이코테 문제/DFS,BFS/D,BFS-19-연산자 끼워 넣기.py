'''
설계
1. 숫자 사이를 노드, 각 연산자 집합을 간선이라 생각하고 완전탐색 돌리기
'''

def dfs(L, cal, cnt):
    if L == N-1:
        if cnt == N-1:
            return res.add(cal)
        return

    for j in range(4):
        if operations[j] > 0:
            operations[j] -= 1
            if j == 0:
                dfs(L+1, cal+nums[L+1], cnt+1)
            if j == 1:
                dfs(L+1, cal-nums[L+1], cnt+1)
            if j == 2:
                dfs(L+1, cal*nums[L+1], cnt+1)
            if j == 3:
                dfs(L+1, int(cal/nums[L+1]), cnt+1)
            operations[j] += 1

N = int(input())
nums = list(map(int,input().split()))
operations = list(map(int,input().split()))
res=set()
dfs(0,nums[0],0)

print(max(res))
print(min(res))