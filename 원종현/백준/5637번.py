import re
li=sorted(re.findall('[A-Z\-a-z]+',open(0).read()[:-1]),key=lambda x:-len(x))
print(li[0].lower())