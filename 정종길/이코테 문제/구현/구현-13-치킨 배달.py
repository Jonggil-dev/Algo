'''
설계
1. 치킨집 M개를 조합으로 만들기
2. 조합별 치킨집을 순회하며 전체 집을 순회 -> 다시 집별 각 조합을 매칭시키고 치킨 최소거리를 구해 가장 작은 값 출력
3. 2번과정 3중 for문 순서 주의! -> 햇갈리면 책 답지처럼 최소거리 구하는 부분은 함수로 빼서 하면 덜 햇갈림
'''

from itertools import combinations

N, M = map(int, input().split())
Arr = [list(map(int,input().split())) for _ in range(N)]
chickens_ls = []
houses = []
for i in range(N):  #2500
    for j in range(N):
        if Arr[i][j] == 2:
            chickens_ls.append((i,j))

        elif Arr[i][j] == 1:
            houses.append((i,j))

chickens_ls = list(combinations(chickens_ls,M))
res = 1e9
# 모든 집을 순회하면서 각 chicken 조합 매칭
for chickens in chickens_ls:
    tmp = 0
    for house in houses:
        x,y = house
        distance = 1e9
        for chicken in chickens:
            i,j = chicken
            distance = min(distance,(abs(x-i) + abs(y-j)))
        tmp += distance
    res = min(res,tmp)

print(res)