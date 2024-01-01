def solution(files):
    files_idx={i:files[i] for i in range(len(files))}
    files={files[i]:i for i in range(len(files))}
    answer = []
    HEAD={}
    NUMBER={}
    NUMBER2={}
    for file in files.keys():
        H,N,T='','',''
        c=0
        for i in file:
            if c==0 and i.isnumeric():
                c=1
            if c==1 and (i.isalpha() or i in '.- '):
                c=2
            if c==0:
                H+=i
            elif c==1:
                if len(N)==5:
                    c=2
                    T+=i
                else:
                    N+=i
            else:
                T+=i
        if H.lower() in HEAD:
            HEAD[H.lower()].append(files[file])
        else:
            HEAD[H.lower()]=[files[file]]
        if int(N) in NUMBER:
            NUMBER[int(N)].append(files[file])
        else:
            NUMBER[int(N)]=[files[file]]
        NUMBER2[files[file]]=[int(N),files[file]]
    for i in sorted(HEAD.keys()):
        tmp=[]
        for j in HEAD[i]:
            tmp.append(NUMBER2[j])
        tmp.sort(key=lambda x:x[0])
        for _,idx in tmp:
            answer.append(files_idx[idx])
    return answer
