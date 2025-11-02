S=input()
word=set(['w'*i+'o'*i+'l'*i+'f'*i for i in range(1,13)])

if S[0]!='w' or len(S)%4!=0:
    print(0)
else:
    st=0
    while True:
        end=st+1
        if end>=len(S):
            break
        while S[end]=='w':
            end+=1
            if end>=len(S):
                print(0)
                exit()
        while S[end]!='w':
            end+=1
            if end>=len(S):
                break
        if S[st:end] not in word:
            print(0)
            exit()
        st=end
    print(1)