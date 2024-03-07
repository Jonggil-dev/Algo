def solution(phone_book):
    answer = True
    n = len(phone_book)
    phone_book.sort()

    for i in range(n-1):
        a=phone_book[i]
        b=phone_book[i+1]
        if a==b[:len(a)]:
            return False

    return answer