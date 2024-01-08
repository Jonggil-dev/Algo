import sys
def check_stack(i):
    if i > 0:
        return 1
    return 0

def append(num):
    global i
    stack[i] = num
    i += 1

def pop():
    global i
    i -= 1
    print(stack[i])


N = int(input())
stack = [0] * N
i = 0
for _ in range(N):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == "1":
        append(order[1])

    elif order[0] == "2":
        if check_stack(i):
            pop()
        else:
            print(-1)

    elif order[0] == "3":
        print(i)

    elif order[0] == "4":
        if check_stack(i):
            print(0)
        else:
            print(1)

    elif order[0] == "5":
        if check_stack(i):
            print(stack[i-1])
        else:
            print(-1)