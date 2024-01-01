'''
설계
1. 오름차순으로 정렬해서 작은 수를 기준으로 그룹 형성 하기
2. 큰수를 기준으로 그룹을 만들면 작은 수 그룹을 먹어 버릴 수 있음
3. ex) 7 3 3 3 2 2 1 -> 이렇게 집단을 만들면 3,3,3 + 2,2 + 1 -> 3set나 먹어버림
'''

nums = list(map(int, input().split()))
nums.sort()
group_cnt = 0
valid_cnt = 0

for num in nums:
    valid_cnt += 1
    if(valid_cnt == num):
        group_cnt += 1
        valid_cnt = 0

print(group_cnt)