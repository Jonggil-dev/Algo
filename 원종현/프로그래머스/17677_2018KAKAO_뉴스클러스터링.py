def solution(str1, str2):
    li1=[]
    dic1={}
    li2=[]
    dic2={}
    for i in range(len(str1)-1):
        word=str1[i:i+2].lower()
        if word.isalpha():
            li1.append(word)
            if word not in dic1:
                dic1[word]=1
            else:
                dic1[word]+=1
    for i in range(len(str2)-1):
        word=str2[i:i+2].lower()
        if word.isalpha():
            li2.append(word)
            if word not in dic2:
                dic2[word]=1
            else:
                dic2[word]+=1
    if not li1 and not li2:
        return 65536
    comb_set=set(li1)&set(li2)
    A=0
    for word in comb_set:
        A+=min(dic1[word],dic2[word])
    C=len(li1)+len(li2)-A
    answer = int((A/C)*65536)
    return answer