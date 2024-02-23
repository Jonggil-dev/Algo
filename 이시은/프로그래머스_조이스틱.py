# 프로그래머스 Lv2 조이스틱

# 알파벳 이름을 완성하기 위해 조이스틱을 조작해야하는 최소 횟수를 구해라
# 처음에는 A*(이름 길이)로 되어 있음
# 위: 다음 알파벳
# 아래: 이전 알파벳(A에서 하면 Z)
# 왼쪽: 커서를 왼쪽으로 이동(가장 왼쪽에서 동작하면 오른쪽 끝으로)
# 오른쪽: 커서를 오른쪽으로 이동(가장 오른쪽에서 동작하면 왼쪽 끝으로)

import copy
def solution(name):
    moves = [-1, 1]
    nameList = list(name)
    # start = (nameList, index, count)
    def bfs(start):
        stack = [start]
        while stack:
            n = stack.pop()
            array, idx, cnt = n[0], n[1], n[2]
            cnt += min(ord(array[idx]) - 65, 91 - ord(array[idx])) # 아스키 코드값으로 변경 횟수 계산
            array[idx] = 'A'
            if array.count('A') == len(array): # 종료 시점
                return cnt
            for move in moves:
                new_array = copy.deepcopy(array) # array 주소 복사 서로 영향 안미치게
                new_idx = idx + move
                new_cnt = cnt + 1
                stack.insert(0, (new_array, new_idx, new_cnt))

    return bfs((nameList, 0, 0))

name = "JEROEN"
# name = "JAN"

print(solution(name))