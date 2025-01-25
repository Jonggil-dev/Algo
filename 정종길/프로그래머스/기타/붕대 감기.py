def solution(bandage, health, attacks):
    continuous = 0
    now = health
    heal = bandage[1]
    maxtime = attacks[-1][0]
    answer = 0
    idx = 0

    for nt in range(1, maxtime + 1):
        continuous += 1

        if nt == attacks[idx][0]:
            now -= attacks[idx][1]
            if now <= 0:
                break
            continuous = 0
            idx += 1
            continue

        now += heal
        if continuous == bandage[0]:
            now += bandage[2]
            continuous = 0

        if now >= health:
            now = health

    if now <= 0:
        answer = -1
    else:
        answer = now

    return answer