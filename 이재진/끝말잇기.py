def solution(n, words):
    answer = []
    words_set = set()
    
    cnt = 0
    for word in words:
        cnt += 1
        if len(words_set) == 0:
            words_set.add(word)
        else:
            if word not in words_set and words[cnt-1][0] == words[cnt-2][-1]:
                words_set.add(word)
            else:
                a = cnt % n
                if a == 0:
                    a = n
                if cnt % n == 0:
                    b = cnt // n
                else:
                     b = cnt // n  + 1
                return [a, b]
    return [0, 0]
