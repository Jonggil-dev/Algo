'''
설계
1. 숫자를 뒤집는 경우의 수는 2가지 -> 부분적으로 or 전체 뒤집기
2. 전체 뒤집기의 경우 의미가 없음. 뒤집으면 그냥 뭉탱이가 적은 숫자만 밖이는 거임
    -> ex 1100110011의경우 0뭉탱이 2개, 1뭉탱이 3개
    -> 전체 뒤집기 -> 0011001100 0뭉탱이 3개, 1뭉탱이 2개
3. 결과적으로 0,1 중 뭉탱이 작은 값 == 뒤집기 최솟값
'''

nums = input()
group0_cnt = 0
group1_cnt = 0
check = nums[0]

if nums[0] == '0':
    group0_cnt += 1
else:
    group1_cnt += 1

for i in range(1,len(nums)):
    if check != nums[i]:
        if nums[i] == '0':
            group0_cnt += 1
        else:
            group1_cnt += 1
        check = nums[i]

res = min(group0_cnt, group1_cnt)
print(res)