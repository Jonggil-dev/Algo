li=[0]*251
li[0]=1
li[1]=1
li[2]=3
for i in range(3,251):
    li[i]=li[i-1]+2*li[i-2]
while True:
    try:
        print(li[int(input())])
    except:
        break