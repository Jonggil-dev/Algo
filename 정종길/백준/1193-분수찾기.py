X = int(input())

# 대각선의 개수를 나타내는 변수
cross = 1

while X > cross:
    X -= cross
    cross += 1

# 대각선의 번호가 홀수인 경우와 짝수인 경우에 따라 계산
if cross % 2 == 0:
    row = X
    column = cross - X + 1
else:
    row = cross - X + 1
    column = X

print(f"{row}/{column}")