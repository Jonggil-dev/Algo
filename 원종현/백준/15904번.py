i=0
for s in input():
    if s=="UCPC"[i]:
        i+=1
    if i>=4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")