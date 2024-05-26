def solution(citations):
    answer = 0
    num = 0
    start, end = 0, max(citations)
    while start <= end:
        mid = (start+end) // 2
        tmp = 0
        for i in citations:
            if mid <= i:
                tmp += 1
        if mid == tmp:
            return mid
        elif mid > tmp:
            end = mid-1
        elif mid <= tmp:
            start = mid+1
            num = mid
    return num
