def solution(n):
    check = bin(n).count("1")

    while True:
        n += 1
        if check == bin(n).count("1"):
            answer = n
            return answer
