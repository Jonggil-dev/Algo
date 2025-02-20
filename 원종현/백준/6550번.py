from collections import deque
import sys
input=sys.stdin.readline

while True:
    try:
        s,t=input().rstrip().split()
        li=deque(list(s))
        for i in t:
            if li and i==li[0]:
                li.popleft()
        print('Yes' if not li else 'No')
    except:
        break