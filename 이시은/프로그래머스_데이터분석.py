# 프로그래머스 Lv1 데이터 분석

# data = ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
# ext 값이 cal_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 return

def solution(data, ext, val_ext, sort_by):
    my_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    answer = []

    for item in data:
        if item[my_dict[ext]] < val_ext:
            answer.append(item)
    answer.sort(key=lambda x: x[my_dict[sort_by]])
    return answer

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"
print(solution(data, ext, val_ext, sort_by))