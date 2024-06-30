from collections import deque
def solution(x, y, n):
    answer = 0
    q = deque()
    q.append([0,x])
    v = set()
    while q:
        ans, now = q.popleft()
        if now == y:
            return ans
        for i in (now+n, now*2, now*3):
            if i <= y and i not in v:
                q.append([ans+1, i])
                v.add(i)
    return -1
