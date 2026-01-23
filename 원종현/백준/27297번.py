import re
print(*['YES'if re.compile('(100+1+|01)+').fullmatch(input())else'NO'for _ in range(int(input()))],sep='\n')