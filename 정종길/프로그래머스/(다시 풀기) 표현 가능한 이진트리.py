def solution(numbers):
    answer = []

    for num in numbers:
        b_num = bin(num)[2:]
        i = 1
        while len(b_num) > 2 ** i - 1:
            i += 1

        b_num = '0' * ((2 ** i - 1) - len(b_num)) + b_num
        if b_num[len(b_num) // 2] == '0':
            answer.append(0)
            continue

        if check_bin(b_num, 1):
            answer.append(1)
        else:
            answer.append(0)

    return answer


def check_bin(b_num, bit):
    parent = len(b_num) // 2

    if bit == '0':
        if b_num[parent] == '1':
            return False

    if len(b_num) == 1:
        return True

    if not check_bin(b_num[:parent], b_num[parent]) or not check_bin(b_num[parent + 1:], b_num[parent]):
        return False
    else:
        return True



