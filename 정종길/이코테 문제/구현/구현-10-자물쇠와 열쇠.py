'''
설계
1. 자물쇠가 가운데 위치하는 자물쇠x3 짜리 크기의 새로운 배열을 두고 열쇠를 회전+이동해가며 풀리는지 맞추기
'''

#2차원 리스트(key) 90도 회전
def rotate_a_matrix_by_90_degree(a):
    N = len(a)
    rotated = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[j][N-i-1] = a[i][j]
    return rotated

#자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length,lock_length * 2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠의 크기를 기존의 3배로 반환
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]


    #4가지 방향에 대해서 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key) #열쇠 회전
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                #새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]


    return False