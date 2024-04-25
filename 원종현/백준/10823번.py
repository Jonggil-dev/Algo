S=''
while True:
    try:
        S+=input()
    except:
        break
print(sum(map(int,S.split(','))))