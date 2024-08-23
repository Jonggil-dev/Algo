def solution(stones, k):
    start = 1
    end = max(stones)

    while start < end:
        mid = (start + end) // 2
        cnt = 0
        for stone in stones:
            if (stone - mid) <= 0:
                cnt += 1
            else:
                cnt = 0
        
            if cnt == k:
                break

        if cnt == k:
            end = mid
        else:
            start = mid + 1

    return start