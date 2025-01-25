def solution(s):
    stack = []
    left_cnt = 0
    for bracket in s:
        if bracket == "(":
            left_cnt += 1
        else:
            if left_cnt:
                left_cnt -= 1
            else:
                return False
    if left_cnt:
        return False

    return True