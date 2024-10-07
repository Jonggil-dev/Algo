def solution(n, tops):
    if tops[0] == 1:
        an = 3
        bn = 4
    else:
        an = 2
        bn = 3

    for i, top in enumerate(tops[1:], start=1):
        if top:
            new_bn = 3 * bn + an
            new_an = 2 * bn + an
        else:
            new_bn = 2 * bn + an
            new_an = bn + an

        bn, an = new_bn, new_an

    answer = bn % 10007

    return answer