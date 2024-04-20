def solution(s):
    answer = True
    left, right = 0, 0
    for i in s:
        if left < right:
            return False
        if i == "(":
            left += 1
        else: 
            right += 1

    if left != right:
        return False
    return True
