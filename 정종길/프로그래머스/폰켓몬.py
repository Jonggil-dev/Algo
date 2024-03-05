def solution(nums):
    num_pick = len(nums) // 2
    ls_types = list(set(nums))
    num_types = len(ls_types)
    # answer = 0
    if num_types <= num_pick:
        answer = num_types
    else:
        answer = num_pick
    return answer