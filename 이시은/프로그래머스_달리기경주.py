# 프로그래머스 lv1 달리기 경주 
# -> 이건 lv1 치고 좀 어려운 듯.. 시간 초과 해결이 관건
# 리스트에서 index를 찾는 것은 O(N)이다!

def solution(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}

    for p in callings:
        # players.index(p) 대신 사용할 수 있는 코드
        c = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[c-1]] += 1 # 불린 선수 앞에 있던 선수는 index가 하나 밀려남
        players[c-1], players[c] = players[c], players[c-1] # 자리 바꿈

    return players



players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))