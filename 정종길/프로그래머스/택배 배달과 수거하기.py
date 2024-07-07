def solution(cap, n, deliveries, pickups):
    answer = 0
    i = j = n - 1

    while i >= 0 or j >= 0:
        truck = cap
        deli_num = pick_num = -1
        box = 0

        while i >= 0:
            if deliveries[i]:
                deli_num = max(deli_num, i)
                box += deliveries[i]
                if box <= cap:
                    deliveries[i] = 0
                else:
                    deliveries[i] = box - cap
                    break
            else:
                i -= 1

        box = 0
        while j >= 0:
            if pickups[j]:
                pick_num = max(pick_num, j)
                box += pickups[j]
                if box <= cap:
                    pickups[j] = 0
                else:
                    pickups[j] = box - cap
                    break
            else:
                j -= 1

        answer += (2 * max(deli_num + 1, pick_num + 1))

    return answer