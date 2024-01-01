'''
설계
1. nums의 길이를 반으로 나누어 왼쪽, 오른쪽 부분 비교
'''
nums = input()
nums_len = len(nums)
res1 = 0
res2 = 0

for i in range(nums_len//2):
    res1 += int(nums[i])

for j in range(nums_len//2,nums_len):
    res2 += int(nums[j])

if res1 == res2:
    print("LUCKY")
else:
    print("READY")