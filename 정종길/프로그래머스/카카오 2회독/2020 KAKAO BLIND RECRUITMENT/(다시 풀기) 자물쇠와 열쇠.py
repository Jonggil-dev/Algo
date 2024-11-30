def solution(key, lock):
    m, n = len(key), len(lock)
    for _ in range(4):
        ex_key = expand_key(key, m, n)
        
        for i in range(n + m - 1):
            for j in range(n + m - 1):
                if insert_key(i, j, n, ex_key, lock):
                    return True

        key = rotate(key)
        
    return False

def expand_key(key, m, n):
    ex_key = []
    for _ in range(n - 1):
        ex_key.append([0] * (m + 2 * n - 2))
    
    for r in range(m):
        row = [0] * (n - 1) + key[r] + [0] * (n - 1) 
        ex_key.append(row)
        
    for _ in range(n - 1):
        ex_key.append([0] * (m + 2 * n - 2))
    
    return ex_key

def insert_key(i, j, n, ex_key, lock):
    for k in range(n):
        for l in range(n):
            if ex_key[i + k][j + l] + lock[k][l] != 1:
                return False
    return True

def rotate(key):  
    rotated = zip(*key[::-1])
    rotated = [list(row) for row in rotated]
    return rotated