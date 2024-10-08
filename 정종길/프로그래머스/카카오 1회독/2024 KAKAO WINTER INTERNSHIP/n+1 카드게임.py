def solution(coin, cards):
    answer = 0
    n = len(cards)
    target = n + 1
    s_pockets = []
    p_pockets = []

    for i in range(n // 3):
        s_pockets.append(cards[i])

    i = n // 3

    while True:
        flag = False
        answer += 1

        for _ in range(2):
            if i >= n:
                return answer

            p_pockets.append(cards[i])
            i += 1

        for card in s_pockets:
            check = target - card
            if check in s_pockets:
                s_pockets.remove(card)
                s_pockets.remove(check)
                flag = True
                break

            if check in p_pockets:
                if coin >= 1:
                    s_pockets.remove(card)
                    p_pockets.remove(check)
                    coin -= 1
                    flag = True
                    break

        if not flag and coin >= 2:
            for card in p_pockets:
                check = target - card
                if check in p_pockets:
                    p_pockets.remove(card)
                    p_pockets.remove(check)
                    coin -= 2
                    flag = True
                    break

        if not flag:
            break

    return answer