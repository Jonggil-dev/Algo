# 프로그래머스 Lv2 광물 캐기

# 5개씩 잘라서 각 곡괭이로 캤을 경우 피로도를 리스트에 담아놓는다
# 돌 곡괭이도 캔 경우 피로도가 가장 높은 순서대로 내림차순으로 정렬한다
# 앞에서부터 되는대로 다이아몬드 곡괭이 -> 철 곡괭이 -> 돌 곡괭이를 배분한다

def solution(picks, minerals):
    tired = []
    my_dict = {'diamond': [1, 5, 25], 'iron': [1, 1, 5], 'stone': [1, 1, 1]}
    i = 0
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    while i < len(minerals):
        if i % 5 == 0 and i != 0:
            tired.append([tmp1, tmp2, tmp3])
            tmp1, tmp2, tmp3 = 0, 0, 0
        target = minerals[i]
        tmp1 += my_dict[target][0]
        tmp2 += my_dict[target][1]
        tmp3 += my_dict[target][2]
        i += 1

    tired.append([tmp1, tmp2, tmp3])
    tired = tired[0:sum(picks)] # 곡괭이 수보다 광물 집합의 수가 많은 경우, 곡괭이 수만큼만 남기기 위함
    tired.sort(key=lambda x: x[-1], reverse=True) # 모든 광물을 돌 곡괭이로 캤을 때의 피로도 순으로 내림차순 정렬함

    pick_idx = 0
    tired_idx = 0
    answer = 0
    while tired_idx < len(tired) and pick_idx < len(picks):
        if picks[pick_idx] != 0:
            answer += tired[tired_idx][pick_idx]
            picks[pick_idx] -= 1
            tired_idx += 1
        else:
            pick_idx += 1

    return answer

picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(picks, minerals))