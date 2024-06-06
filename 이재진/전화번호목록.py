def solution(phone_book):
    answer = True
    dic = {i:1 for i in phone_book}
    for num in phone_book:
        tmp = ""
        for i in num:
            tmp += i
            if tmp in dic.keys() and tmp != num:
                return False      
    return answer
