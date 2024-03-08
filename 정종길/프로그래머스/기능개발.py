def solution(progresses, speeds):
    answer = []
    N = len(progresses)
    day = 1
    cnt = 0

    for i in range(N):
        if progresses[i] + (speeds[i] * day) >= 100:
            cnt += 1

        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0

            while progresses[i] + (speeds[i] * day) < 100:
                day += 1
            cnt += 1

        if i == N - 1:
            answer.append(cnt)

    return answer