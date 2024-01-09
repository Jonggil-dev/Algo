# 프로그래머스 가장 많이 받은 선물

def solution(friends, gifts):
    N = len(friends)
    board = [[0] * N for _ in range(N)]
    count = [0] * N
    for gift in gifts:
        give, take = gift.split()
        board[friends.index(give)][friends.index(take)] += 1

    for i in range(1, N):
        for j in range(i):
            if board[i][j] < board[j][i]: # 주고 받은 선물 수가 차이나는 경우 -> 많이 준 쪽이 선물 받기
                count[j] += 1
            elif board[i][j] > board[j][i]: # 주고 받은 선물 수가 차이나는 경우 -> 많이 준 쪽이 선물 받기
                count[i] += 1
            else: # 차이나지 않는 경우 -> 선물 지수 비교
                a = sum(board[i]) - sum(list(zip(*board))[i])
                b = sum(board[j]) - sum(list(zip(*board))[j])
                if a > b:
                    count[i] += 1
                elif a < b:
                    count[j] += 1
                else:
                    continue

    # print(board)
    # print(count)
    return max(count)

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(friends, gifts))