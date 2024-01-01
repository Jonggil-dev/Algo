'''
설계
1. 0~9 중에서는 곱하기에 0, 1이 포함되어 있는게 아니면 곱하는게 더하는 거보다 값이 큼
2. 2의 경우는 2+2 == 2*2
3. 위 두가지 말고는 예외 케이스 없음
'''

nums = input()
res = 0
for num in nums:
    num = int(num)
    if num <= 1 or res <= 1:
        res += num
    else:
        res *= num

print(res)