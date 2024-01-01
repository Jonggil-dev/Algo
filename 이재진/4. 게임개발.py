N, M = map(int, input().split())
A, B, d = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(N)]
d_xy = [(-1,0), (0,-1), (1,0), (0,1)]
now = [A, B]
cnt = 1
ls[A][B] = 1
while True:
    flag = 0
    for i in range(4):
        d = (d+i)%4
        next = [now[0]+d_xy[d][0], now[1]+d_xy[d][1]]
        if ls[next[0]][next[1]] == 1:
            flag += 1
        else:
            now = next
            ls[now[0]][now[1]] = 1
            cnt += 1
            break
    if flag == 4:
        break
print(cnt)