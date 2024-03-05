# 프로그래머스 lv2 테이블 해시 함수

# col 기준으로 data 정렬
# row_begin에서 row_end까지 data의 tuple의 각 원소를 row로 나눈 나머지의 합
# 해당 값들을 누적하여 bitwise XOR한 값

def solution(data, col, row_begin, row_end):
    data = sorted(data, key=lambda x:(x[col-1], -x[0]))
    answer = 0
    for row in range(row_begin, row_end+1):
        mod_sum = 0
        for item in data[row-1]:
            mod_sum += item % row
        answer = answer ^ mod_sum
    return answer

data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
print(solution(data, 2, 2, 3))