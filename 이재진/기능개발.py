from collections import deque
def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    progresses, speeds = deque(progresses), deque(speeds)
    while speeds:
        for i in range(n):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            print(progresses)
            cnt = 0
            while progresses and progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                cnt += 1
            answer.append(cnt)
            n -= cnt
    return answer