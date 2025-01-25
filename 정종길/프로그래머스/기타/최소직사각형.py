def solution(sizes):
    answer = 0
    min_w = min_h = 0

    for w, h in sizes:
        min_w = max(min_w, w, h)
        min_h = max(min_h, min(w, h))

    answer = min_w * min_h

    return answer