import sys
sys.setrecursionlimit(10000)

def solution(n, m, x, y, r, c, k):
    global answer, delta
    
    answer = ""
    delta = [(1, 0), (0, -1), (0, 1), (-1, 0)] #dlru 오름차순
    
    (sx, sy), (ex, ey) = (x - 1, y - 1), (r - 1, c - 1)
    
    dfs(sx, sy, ex, ey, 0, k, n, m, "")
        

    if not answer:
        return "impossible"
    
    return answer

def dfs(hi, hj, ex, ey, cnt, k, n, m, txt):
    global answer, delta
    
    # 남은 거리 + cnt가 k 보다 클 경우 종료
    if k - cnt < (abs(hi - ex) + abs(hj - ey)):
        return
    
    # k에 도착 했는데 남은 횟수가 짝수가 아니 라면 탈출 불가능
    if (k - abs(hi - ex) + abs(hj - ey) + cnt) % 2:
        return 
    
    # k에 도착 하고 cnt == k라면 함수 종료 dfs + dlru 문자열 오름차순 순서로 순회하기 떄문에 첫 번 째 탈출이 가장 사전 순으로 빠름  
    if (hi, hj) == (ex, ey) and cnt == k:
        answer = txt
        return True
    
    for d in range(4):
        ni, nj = hi + delta[d][0], hj + delta[d][1]
        if 0 <= ni < n and 0 <= nj < m:
            if d == 0:
                if dfs(ni, nj, ex, ey, cnt + 1, k, n, m, txt + "d"):
                    return True
            elif d == 1:
                if dfs(ni, nj, ex, ey, cnt + 1, k, n, m, txt + "l"):
                    return True
            elif d == 2:
                if dfs(ni, nj, ex, ey, cnt + 1, k, n, m, txt + "r"):
                    return True
            else:
                if dfs(ni, nj, ex, ey, cnt + 1, k, n, m, txt + "u"):
                    return True