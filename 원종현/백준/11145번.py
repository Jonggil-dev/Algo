for _ in range(int(input())):
    try:
        S=int(input().strip())
        print(S if S>=0 else 'invalid input')
    except:
        print('invalid input')