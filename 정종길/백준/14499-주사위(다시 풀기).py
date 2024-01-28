n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dice = [0] * 6  # 주사위의 여섯 면

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# dice는 항상 주사위의 [윗면, 북, 동, 서, 남, 아랫면] 순서로 요소를 가짐
# rotate 배열은 주사위의 윗면(0), 북(1), 동(2), 서(3) ,남(4) , 아랫면(5)에 해당하는 인덱스를 나타내는 거임
# 주사위를 동쪽으로 굴리면 처음의 "서, 북, 윗면, 아랫, 남, 동" 순서로 [윗면, 북, 동, 서, 남, 아랫면] 형태가 됨
# 주사위를 서쪽, 북쪽으로 굴렸을 때를 생각해보면 아래 rotate와 같은 인덱스 배열을 만들 수 있음
rotate = [
    [3, 1, 0, 5, 4, 2],  # 동
    [2, 1, 5, 0, 4, 3],  # 서
    [4, 0, 2, 3, 5, 1],  # 북
    [1, 5, 2, 3, 0, 4]   # 남
]

def roll_dice(direction):
    global dice
    dice = [dice[rotate[direction-1][i]] for i in range(6)]

def move(x, y, direction):
    nx, ny = x + dx[direction-1], y + dy[direction-1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return x, y, False
    return nx, ny, True

for command in commands:
    x, y, is_valid = move(x, y, command)
    if not is_valid:
        continue
    roll_dice(command)
    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5] = board[x][y]
        board[x][y] = 0
    print(dice[0])