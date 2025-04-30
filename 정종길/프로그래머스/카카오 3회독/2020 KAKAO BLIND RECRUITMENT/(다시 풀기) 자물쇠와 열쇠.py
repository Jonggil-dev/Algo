'''
1. 큰 그림은 lock의 상하좌우를 확장했다 생각하고, key를 확장한 부분의 0,0 부터 끝까지 순회하며 key로 구멍을 맞춰보면 모든 경우의 수 비교가 됨 (key 회전도 하기)
2. 근데 위의 과정을 직접 배열로 처리하는게 아니라, lock의 구멍과 key의 블록만 비교하면 되니까 좌표 값만 빼와서 비교하는거임
'''
def solution(key, lock):
    m, n = len(key), len(lock)
    keys, holes = set(), set()
    
    for i in range(m):
        for j in range(m):
            if key[i][j] == 1:
                keys.add((i, j))
    
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                holes.add((i + m - 1, j + m - 1))
    
    
    for _ in range(4):
        if put_key(keys, holes, m , n):
            return True
        keys = rotate(keys, m)
    return False

def rotate(keys, m):
    r_keys = set()
    for x, y in keys:
        r_keys.add((y, m - x - 1))
    return r_keys

def put_key(keys, holes, m, n):
    for i in range(m - 1 + n):
        for j in range(m - 1 + n):
            cnt, flag = 0, True
            
            for ki, kj in keys:
                ni, nj = ki + i, kj + j
                if (ni, nj) in holes:
                    cnt += 1
                elif m - 1 <= ni < n + m - 1 and m - 1 <= nj < n + m - 1:
                    flag = False
                    break
                    
            if flag and cnt == len(holes):
                return True
            
    return False
    