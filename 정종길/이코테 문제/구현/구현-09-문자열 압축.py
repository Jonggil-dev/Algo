'''
설계
1. 문자열 1개씩 검사, 2개씩 검사 ... 등 step을 나누어 구현하기
2. step을 증가시키는 for문, 문자열을 순회하는 for문 2가지의 2중 for문 구현
'''

def solution(s):
    answer = len(s)

    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        cnt = 1

        for j in range(step,len(s),step):
            if prev == s[j:j+step]: #j+step이 문자열 길이를 초과해도 에러 안뜨고 문자열 마지막까지만 반영됨
                cnt += 1

            else:
                if cnt >= 2:
                    compressed += (str(cnt) + prev)
                else:
                    compressed += prev
                prev = s[j:j+step]
                cnt = 1

        # 각 step 별로 맨 마지막 구간 문자열 부분 처리로직
        if cnt >= 2:
            compressed += (str(cnt) + prev)
        else:
            compressed += prev
        print(compressed)
        answer = min(answer,len(compressed))

    return answer

print(solution('abcabcabcabcdededededede'))