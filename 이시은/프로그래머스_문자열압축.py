def solution(s):
    if len(s) == 1:
        return 1

    answer = float("inf")
    for n in range(1, len(s)//2+1):
        partial = s[0:n]
        tmp = ''
        cnt = 1
        idx = n
        while idx < len(s):
            if partial == s[idx:idx+n] :
                cnt += 1
                idx += n
            else:
                if cnt >= 2:
                    tmp = tmp + str(cnt) + partial
                else:
                    tmp += partial
                partial = s[idx:idx+n]
                idx += n
                cnt = 1
        if idx >= len(s):
            tmp = tmp + str(cnt) + partial if cnt >= 2 else tmp + partial
        answer = min(answer, len(tmp))
    return answer

s = "aabbaccc"
s = "ababcdcdababcdcd"
s = "abcabcdede"
s = "abcabcabcabcdededededede"
s = "xababcdcdababcdcd"
print(solution(s))