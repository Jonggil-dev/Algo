'''
1. 주어진 수를 포화 이진트리 형태의 이진수로 표현하기
2. 포화 이진트리 + "리프 노드가 아닌 노드는 자신의 왼쪽 자식이 ~ " 이 부분을 생각해 보면
-> 서브 트리의 루트 노드는 항상 이진 수 문자열 중 가운데 위치
3. 즉 전체 문자열에서 절반 씩 나누어 가며, 루트노드가 0인데 자식 노드가 1인 경우가 나오면 실패
'''
def solution(numbers):
    answer = []
    for num in numbers:
        num = to_pbt(num)
        answer.append(valid_check(num, -1))
        
    return answer

def to_pbt(num):
    num = bin(num)[2:]
    level = 1
    
    while len(num) > 2 ** level - 1:
        level += 1
    
    full_cnt = 2 ** level - 1
    return "0" * (full_cnt - len(num)) + num

def valid_check(num, root):
    mid = len(num) // 2

    if root == "0" and num[mid] == "1":
        return 0
    
    if len(num) == 1:
        return 1
    
    left_sub, right_sub = num[ : mid], num[mid + 1: ]
    
    if not valid_check(left_sub, num[mid]) or not valid_check(right_sub, num[mid]):

        return 0
    
    return 1
    
    