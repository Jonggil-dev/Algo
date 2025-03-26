'''
1. n단계 유사 칸토어 비트열의 총 길이는 5 ^ n
2. n단계 유사 칸토어 비트열을 S(n)이라고 한다면,
유사 칸토어 비트열은 S(n-1) + S(n-1) + 00000 + S(n-1) + S(n-1) 형태로 이루어져 있음
3. 결국 n-1 단계의 "0"에서 뻗어나온 범위들은 모두 0임
-> 이거를 반대로 추적해서 문제를 품

풀이방법
1. n단계 유사 칸토어 비트열은 5등분(1,2,3,4,5파트)으로 쪼개기
2. 구하고자 하는 범위가 가운데(3파트)에 해당하면 이전의 0에서 뻗어나온 것이므로 0임
3. 구하고자 하는 범위가 가운데가 아니라면, 해당하는 파트를 다시 5등분으로 쪼개서 범위가 쪼갠 범위의 가운데 파트에 해당하는지 재귀로 확인 
'''

def solution(n, l, r):
    return count_ones(1, 5 ** n, l, r)


def count_ones(start, end, l, r):
    
    if r < start or end < l:
        return 0

    if start == end:
        return 1

    length = (end - start + 1) // 5
    total = 0

    for i in range(5):
        if i == 2:
            continue
        part_start = start + i * length
        part_end = part_start + length - 1

        total += count_ones(part_start, part_end, l, r)

    return total