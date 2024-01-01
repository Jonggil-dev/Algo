'''
설계
1. 이중 for문으로 i, j 무게가 같은 경우만 빼고 전부 탐색
'''

N, M = map(int, input().split())
nums = list(map(int,input().split()))
res = 0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] == nums[j]:
            continue
        res += 1
print(res)