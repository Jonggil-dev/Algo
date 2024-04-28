def solution(s):
    cnt_0 = 0
    cnt_trans = 0

    while s != "1":
        cnt_1 = s.count("1")
        cnt_0 += s.count("0")

        s = bin(cnt_1)[2:]
        cnt_trans += 1

    answer = [cnt_trans, cnt_0]
    return answer