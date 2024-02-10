# 프로그래머스 lv1 신고결과받기
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    my_dict = {}
    for id in id_list:
        my_dict[id] = []

    acc = {}
    for re in report:
        FROM, TO = re.split()
        if TO not in my_dict[FROM]:
          my_dict[FROM].append(TO)
          if TO in acc.keys():
              acc[TO] += 1
          else:
              acc[TO] = 1


    for key, value in acc.items():
        if value >= k:
          for n in range(len(id_list)):
              if key in my_dict[id_list[n]]:
                  answer[n] += 1        
        
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
print(solution(id_list, report, k))

