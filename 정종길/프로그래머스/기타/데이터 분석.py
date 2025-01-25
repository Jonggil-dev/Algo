def solution(data, ext, val_ext, sort_by):
    answer = []
    text = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    idx = text[ext]
    data.sort(key=lambda x: x[text[sort_by]])
    for row in data:
        if row[idx] < val_ext:
            answer.append(row)

    return answer