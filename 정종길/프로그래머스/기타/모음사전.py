def dfs(dict_word, leng, word):
    global answer
    answer += 1

    if dict_word == word:
        return True

    if leng == 5:
        return False

    for alpha in alphas:
        if dfs(dict_word + alpha, leng + 1, word):
            return True


def solution(word):
    for i in range(5):
        if dfs(alphas[i], 1, word):
            break

    return answer


alphas = ["A", "E", "I", "O", "U"]
answer = 0