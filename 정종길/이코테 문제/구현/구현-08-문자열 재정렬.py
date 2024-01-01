'''
설계
1. 입력값을 순회하면서 숫자면 더하고 문자면 따로 모아서 정렬하기
2. 입력값에 숫자는 0만 있는경우와 숫자가 아예 없는경우를 분리 해야됨
'''
texts = input()
num_sum = 0
flag = False
res = []

for text in texts:
    if text.isdigit():
        num_sum += int(text)
        flag = True
    else:
        res.append(text)

res.sort()

if flag:
    res = res + [str(num_sum)]

print(''.join(res))