from itertools import product


def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    perms = list(product(discounts, repeat=len(emoticons)))
    answer = [0, 0]

    for perm in perms:
        total_price = 0
        cnt = 0

        for user in users:
            dis = user[0]
            adjust_price = user[1]
            price = 0

            for i in range(len(perm)):
                if perm[i] >= dis:
                    price += ((100 - perm[i]) * emoticons[i] / 100)

            if price >= adjust_price:
                cnt += 1

            else:
                total_price += price

        if answer[0] < cnt:
            answer[0] = cnt
            answer[1] = total_price

        elif answer[0] == cnt:
            if answer[1] < total_price:
                answer[1] = total_price

    return answer