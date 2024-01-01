# 프로그래머스 시소 짝궁

import math
from itertools import combinations

def solution(weights):
    # 같은 수 있는지 확인하고 하나만 남기고 제거 O(N)
    unique_weight = [weights[0]]

    same_dict1 = {} # weights에 같은 수가 있으면, 어떤 수가 몇 번 나오는지 기록하는 딕셔너리
    for w in weights[1:]:
        if w in unique_weight:
            same_dict1[w] = same_dict1.get(w, 1) + 1
        else:
            unique_weight.append(w)

    # print(same_dict1)

    # 2, 3, 4를 곱한 값을 이어 붙이기
    multiply_weight = [i * 2 for i in unique_weight] + [i * 3 for i in unique_weight] + [i * 4 for i in unique_weight]

    # print(multiply_weight)

    # 앞에서부터 하나씩 꺼내서 뒤에 같은 값 있는지 확인
    i = 0
    same_dict2 = {}
    while i < len(multiply_weight) - 1:
        w = multiply_weight[i]
        if w in multiply_weight[i+1:]: # 같은 값이 뒤에 존재하면, same_dict2에 key를 추가하고 value는 빈 리스트로 설정
            same_dict2[w] = []
        i += 1

    for key in same_dict2.keys(): # 같은 값이 존재하는 수에 대해서, 2, 3, 4로 나눈 뒤 unique_weight에 있는 값인지 확인하고, 있으면 same_dict2[key]에 추가한다
        if key / 2 in unique_weight:
            same_dict2[key].append(int(key/2))
        if key / 3 in unique_weight:
            same_dict2[key].append(int(key/3))
        if key / 4 in unique_weight:
            same_dict2[key].append(int(key/4))

    cnt = 0
    for value in same_dict2.values():
        if len(value) >= 3:
            # value가 3개 이상이면 2개를 뽑는 경우의 수가 1보다 커진다
            # -> combinations를 이용해서 2개 뽑는 경우를 모두 구하고,
            # 원본 배열에서 중복이 있었는지 확인하고, 있다면 중복 갯수를 곱해주는 방식으로 계산
            combs = list(combinations(value, 2))
            tmp = 0
            for comb in combs:
                tmp += same_dict1.get(comb[0], 1) * same_dict1.get(comb[1], 1) # 중복이 없었다면 1이 곱해지는 것

        else:
            tmp = same_dict1.get(value[0], 1) * same_dict1.get(value[1], 1) # 여기도 마찬가지로 원본 배열에 중복이 있다면 중복 숫자의 갯수, 없다면 1이 곱해짐

        # print(value, tmp)
        cnt += tmp

    for value in same_dict1.values(): # 처음 weights에서 동일한 값이 있던 수에 대해서 해당 수 중 2개를 고르는 경우의 수를 cnt에 더해준다
        cnt += math.comb(value, 2)

    # print(same_dict2)
    return cnt


weights = [100, 100, 180, 360, 270]
weights = [100, 100, 100, 150, 150, 200, 300]
# weights = [100, 100, 180, 180, 360, 100, 270]
print(solution(weights))