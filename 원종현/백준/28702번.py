li=[input() for _ in range(3)]
res=0
for i in range(2,-1,-1):
    if li[i].isdigit():
        res=int(li[i])+(3-i)
        break

if res%15==0:
    print('FizzBuzz')
elif res%3==0:
    print('Fizz')
elif res%5==0:
    print('Buzz')
else:
    print(res)