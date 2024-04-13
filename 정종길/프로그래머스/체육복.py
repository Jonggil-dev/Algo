def solution(n, lost, reserve):
    valid_lost = [0] * (n + 1)
    valid_res = [0] * (n + 1)

    lost.sort()
    reserve.sort()

    for lost_st in lost:
        for res_st in reserve:
            if lost_st == res_st:
                valid_res[res_st] = 1
                valid_lost[lost_st] = 1
                break

            if res_st > lost_st:
                break

    for lost_st in lost:
        for res_st in reserve:
            if res_st < (lost_st - 1):
                continue

            if res_st > (lost_st + 1):
                break

            if not valid_lost[lost_st] and not valid_res[res_st]:
                valid_lost[lost_st] = 1
                valid_res[res_st] = 1
                break

    return n - len(lost) + valid_lost.count(1)