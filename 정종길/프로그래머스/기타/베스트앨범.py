def solution(genres, plays):
    answer = []

    generes_cnt = {}
    plays_sort = []

    for i in range(len(genres)):
        if genres[i] not in generes_cnt:
            generes_cnt[genres[i]] = plays[i]
        else:
            generes_cnt[genres[i]] += plays[i]
        plays_sort.append((genres[i], plays[i], i))

    first_sorted = sorted(plays_sort, key=lambda x: -x[1])
    second_sorted = sorted(first_sorted, key=lambda x: x[0])
    generes_rank = sorted(generes_cnt, key=generes_cnt.get, reverse=True)

    for genere in generes_rank:
        cnt = 0
        for genere_check, _, index in second_sorted:
            if genere == genere_check:
                answer.append(index)
                cnt += 1
            if cnt == 2:
                break

    return answer