def solution(n, times):
    times.sort()
    start_time = 1
    end_time = times[-1] * n

    while start_time <= end_time:
        mid = (start_time + end_time) // 2
        if check_valid(mid, times, n):
            end_time = mid - 1
        else:
            start_time = mid + 1

    return start_time


def check_valid(mid, times, n):
    peoples = 0
    for time in times:
        peoples += mid // time
        if peoples >= n:
            return True
    return False