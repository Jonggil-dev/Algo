# baekjoon 2149 암호 해독

import sys

input = sys.stdin.readline

key = list(map(list, input().strip()))
code = input().strip()
N = int(len(code) / len(key))

col_code = []
for i in range(len(key)):
    key[i].append(i)
    col_code.append(code[i*N: (i+1)*N])
key = sorted(key, key=lambda x: x[0])


org = ''
for j in range(N):
    tmp = [0] * len(key)
    for k, key_item in enumerate(key):
        tmp[key_item[1]] = col_code[k][j]

    org += ''.join(tmp)