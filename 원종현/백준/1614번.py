a=int(input())
b=int(input())
if 2<=a<=4:
    if not b%2:
        print((b*4)+(a-1))
    else:
        print((b*4)+(5-a))
elif a==1:
    print(b*8)
else:
    print(b*8+4)