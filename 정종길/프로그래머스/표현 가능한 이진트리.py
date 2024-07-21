def solution(numbers):
    answer = []
    for number in numbers:
        bin_num = make_pbt(bin(number)[2:])
        if is_valid(bin_num, 1):
            answer.append(1)
        else:
            answer.append(0)
    return answer


def make_pbt(number):
    i = 1
    while len(number) > (2 ** i - 1):
        i += 1

    return "0" * (2 ** i - 1 - len(number)) + number


def is_valid(bin_num, pre_root):
    root_idx = len(bin_num) // 2
    now_root = bin_num[root_idx]

    if pre_root == "0" and now_root == "1":
        return False

    if len(bin_num) == 1:
        return True

    if not is_valid(bin_num[:root_idx], now_root) or not is_valid(bin_num[root_idx + 1:], now_root):
        return False

    return True