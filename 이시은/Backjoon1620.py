# Backjoon 1620 나는야 포켓몬 마스터 이다솜
# 리스트보다는 딕셔너리가 속도가 빠르다!

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict_name = {}
dict_number = {}
for i in range(N):
    name = input().strip()
    dict_name[name] = i+1
    dict_number[i+1] = name

answer = []
for _ in range(M):
    quiz = input().strip()
    if quiz.isdigit():
        print(dict_number[int(quiz)])
    else:
        print(dict_name[quiz])

