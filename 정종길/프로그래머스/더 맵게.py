import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2:
        fir = heapq.heappop(scoville)

        if fir >= K:
            return answer

        sec = heapq.heappop(scoville)
        heapq.heappush(scoville, fir + (sec * 2))
        answer += 1

    if scoville[0] >= K:
        return answer

    return -1
