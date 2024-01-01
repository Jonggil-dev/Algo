# 프로그래머스 부분수열의 합

# 완전 탐색 -> 최소힙 개념 -> O(N)만 나오게 해보자
"""
# 시간초과 풀이
import heapq

def solution(seq, k):
    idx_heap = []

    MIN = len(seq)
    for i in range(len(seq)):
        SUM = 0
        j = i
        while SUM < k and j < len(seq) and (j-i) <= MIN:
            SUM += seq[j]
            j += 1
            if SUM > k:
                break

        if SUM == k:
            j -= 1
            heapq.heappush(idx_heap, [j-i, i, j])
            # idx_list.append([j-i, i, j])
            MIN = min(j-i, MIN)

    # idx_list.sort(key=lambda x: (len(x), x[0]))
    # print(idx_list)
    # answer = [idx_list[0][1], idx_list[0][2]]
    # print(idx_heap)
    answer = heapq.heappop(idx_heap)
    return answer

"""


def solution(seq, k):
    if k in seq:
        return [seq.index(k), seq.index(k)]
    SUM = 0
    start = 0
    MIN = len(seq)
    answer = False
    for i in range(len(seq)):
        if SUM == k:
            if (i - start - 1) < MIN:
                answer = [start, i-1]
                MIN = i - start - 1

        SUM += seq[i]
        if SUM < k:
            continue

        while SUM > k:
            SUM -= seq[start]
            start += 1

    if not answer and SUM == k:
        answer = [start, len(seq)-1]

    return answer



seq = [1,2,3,4,5]
k = 7
seq = [1,1,1,2,3,4,5]
k = 5
seq = [2,2,2,2,2]
k = 6
seq = [2, 2, 2, 2, 2, 10, 10, 10, 10, 10, 10]
k= 30
seq = [1,1,1,1,1,1,1]
k = 7
print(solution(seq, k))


