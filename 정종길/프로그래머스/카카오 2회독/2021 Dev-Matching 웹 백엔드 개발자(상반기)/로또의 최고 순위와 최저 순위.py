def solution(lottos, win_nums):
    answer = []
    win_nums = set(win_nums)
    zero = win = 0
    rank = { i : (7 - i if i != 0 else 6) for i in range(7) }
    for num in lottos:
        if num == 0:
            zero += 1
            continue
            
        if num in win_nums:
            win += 1
            win_nums.remove(num)
    
    answer = [rank[win + min(zero, len(win_nums))], rank[win]]
    
    return answer