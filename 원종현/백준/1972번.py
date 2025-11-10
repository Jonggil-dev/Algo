while True:
    S=input()
    if S=='*':
        break

    for i in range(1,len(S)-1):
        tmp=set()
        for j in range(len(S)-i):
            pair=S[j]+S[i+j]
            if pair in tmp:
                print(S,"is NOT surprising.")
                break
            else:
                tmp.add(pair)
        else:
            continue
        break
    else:
        print(S,'is surprising.')