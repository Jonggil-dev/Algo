import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        tmp = a + (b * 2)
        heapq.heappush(scoville, tmp)
        answer += 1
    if scoville[0] < K:
        return -1
    return answer
