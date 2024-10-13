def solution(n):
    ls = [i for i in str(n)]
    answer = []
    for i in range(len(ls)):
        answer.append(int(ls.pop()))
    return answer
