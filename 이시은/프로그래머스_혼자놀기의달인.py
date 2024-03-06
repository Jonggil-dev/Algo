# 프로그래머스 lv2 혼자 놀기의 달인

def solution(cards):
    groups = []
    used = []

    for card in cards:
        if set(cards) & set(used) == set(cards):
            break

        sub_group = []
        while True:
            if card in used:
                groups.append(sub_group)
                break
            sub_group.append(card)
            used.append(card)
            card = cards[card-1]

    if len(groups) == 1:
        return 0
    else:
        groups.sort(key=lambda x: -len(x))
        return len(groups[0]) * len(groups[1])


print(solution([8,6,3,7,2,5,1,4]))