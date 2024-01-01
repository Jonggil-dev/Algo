'''
설계
1. dfs로 장애물 3개 모든 경우의 수 설치해보고 설치 될 때마다 확인하기
2. 시간복잡도, 배열 6*6
    (1) dfs -> L = 0,1,2 일때 각 36 순회 -> 36^3
    (2) L=3 일때 check_boserve -> 최악의 경우 teachers =36개일때 -> 36*4*6
    (3) 최종 -> (36*3)*(36*4*6)
3. 중복된 탐색을 피하기 위해 dfs for문 range범위 하기와 같이 작성함
    (1) i,j 순회하는 로직은 조합을 만드는 로직과 동일하게 순회해야 됨 -> 즉, i,j는 뒤쪽으로만 증가시키면서 탐색하면 됨
'''
def check_observe(Arr):
    for i,j in teachers:
        for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
            for k in range(1,N):
                ni, nj = i+(di*k), j+(dj*k)
                if ni < 0 or nj < 0 or ni >= N or nj >= N:
                    break
                if Arr[ni][nj] == "O":
                    break
                if Arr[ni][nj] == "S":
                    return False
    return True

def dfs(L, x, y):
    if L == 2:
        return check_observe(Arr)

    for i in range(x, N):
        for j in range(y if i == x else 0, N):
            if Arr[i][j] == "X":
                Arr[i][j] = "O"
                if dfs(L + 1, i, j + 1):
                    return True
                Arr[i][j] = "X"

    return False

N = int(input())
Arr = [list(input().split()) for _ in range(N)]
teachers = []
for i in range(N):
    for j in range(N):
        if Arr[i][j] == "T":
            teachers.append((i,j))

if dfs(0,0,0):
    print("YES")
else:
    print("NO")