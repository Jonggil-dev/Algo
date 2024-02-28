def solution(keymap, targets):
    dic = {}
    for key in keymap:
        for j in range(len(key)):
            if key[j] not in dic:
                dic[key[j]] = j+1
            elif key[j] in dic and dic[key[j]] > j+1:
                dic[key[j]] = j+1
    answer = [0]*len(targets)
    for i in range(len(targets)):
        for j in targets[i]:
            if j in dic:
                answer[i] += dic[j]
            else:
                answer[i] = -1
                break
    return answer
