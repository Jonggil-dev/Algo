import sys
N = int(sys.stdin.readline())
ls = [list(sys.stdin.readline().split()) for _ in range(N)]
max_num = -float("inf")
min_num = float("inf")
def dfs(start, cur_num, op):
    global max_num, min_num
    if start[0] == N-1 and start[1] == N-1:
        if max_num < cur_num:
            max_num = cur_num
        if min_num > cur_num:
            min_num = cur_num
        return
    for d in [(0,1), (1,0)]:
        ni, nj = start[0] + d[0], start[1] + d[1]
        if 0 <= ni < N and 0 <= nj < N:
            next_item = ls[ni][nj]
            if next_item.isnumeric():
                if op == "+":
                    tmp = cur_num + int(ls[ni][nj])
                    dfs((ni, nj), tmp, op)
                elif op == "-":
                    tmp = cur_num - int(ls[ni][nj])
                    dfs((ni, nj), tmp, op)
                elif op == "*":
                    tmp = cur_num * int(ls[ni][nj])
                    dfs((ni, nj), tmp, op)
            else:
                dfs((ni, nj), cur_num, ls[ni][nj])
dfs((0, 0), int(ls[0][0]),"")
print(max_num, min_num)