from collections import deque
N = int(input())
command = [input().split() for _ in range(N)]
ls = deque()
for com in command:
    if com[0] == 'push_front':
        ls.appendleft(int(com[1]))
    elif com[0] == 'push_back':
        ls.append(int(com[1]))
    elif com[0] == 'pop_front':
        if not ls:
            print(-1)
        else:
            print(ls.popleft())
    elif com[0] == 'pop_back':
        if not ls:
            print(-1)
        else:
            print(ls.pop())
    elif com[0] == 'size':
        print(len(ls))
    elif com[0] == 'empty':
        if len(ls):
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if not ls:
            print(-1)
        else:
            print(ls[0])
    elif com[0] == 'back':
        if not ls:
            print(-1)
        else:
            print(ls[-1])
