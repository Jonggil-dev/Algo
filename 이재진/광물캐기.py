from collections import deque
import copy

def algo(picks, ls, ans):
    if not ls or sum(picks) == 0:
        return ans
    a,b,c = float("inf"), float("inf"), float("inf")
    if ls and picks[0] > 0:
        new_picks = copy.deepcopy(picks)
        new_ls = copy.deepcopy(ls)
        new_ans = ans
        new_picks[0] -= 1
        now = new_ls.popleft()
        new_ans += len(now)
        a = algo(new_picks, new_ls, new_ans)
    if ls and picks[1] > 0:
        new_picks = copy.deepcopy(picks)
        new_ls = copy.deepcopy(ls)
        new_ans = ans
        new_picks[1] -= 1
        now = new_ls.popleft()
        for i in now:
            if i == "diamond":
                new_ans += 5
            else:
                new_ans += 1
        b = algo(new_picks, new_ls, new_ans)
    if ls and picks[2] > 0:
        new_picks = copy.deepcopy(picks)
        new_ls = copy.deepcopy(ls)
        new_ans = ans
        new_picks[2] -= 1
        now = new_ls.popleft()
        for i in now:
            if i == "diamond":
                new_ans += 25
            elif i == "iron":
                new_ans += 5
            elif i == "stone":
                new_ans += 1
        c = algo(new_picks, new_ls, new_ans)
    
    return min(a, b, c)


def solution(picks, minerals):
    answer = 0
    ls = deque()
    tmp = []
    cnt = 0
    for m in minerals:
        tmp.append(m)
        cnt += 1
        if cnt == 5:
            ls.append(tmp)
            tmp = []
            cnt = 0
    if tmp:
        ls.append(tmp)
    answer = algo(picks, ls, 0)

    return answer
