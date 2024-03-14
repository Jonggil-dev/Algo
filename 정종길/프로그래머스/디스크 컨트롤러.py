import heapq

def solution(jobs):
    answer = []
    jobs.sort(key=lambda x: x[0])
    time = jobs[0][0]
    buffer = []
    i = 0

    while i < len(jobs):
        while i < len(jobs) and jobs[i][0] <= time:
            heapq.heappush(buffer, (jobs[i][1], jobs[i][0]))
            i += 1

        if buffer:
            work_span, work_start = heapq.heappop(buffer)
            time += work_span
            answer.append(time - work_start)
            continue

        time += 1

    while buffer:
        work_span, work_start = heapq.heappop(buffer)
        time += work_span
        answer.append(time - work_start)

    answer = sum(answer) // len(jobs)

    return answer