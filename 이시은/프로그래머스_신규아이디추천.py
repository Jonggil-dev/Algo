# 프로그래머스 lv1 신규 아이디 추천

# 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발
# 규칙
# - 아이디의 길이는 3자 이상 15자 이하
# - 아이디는 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 문자만 사용할 수 있음
# - 마침표는 처음과 끝에 사용할 수 없고 연속으로 사용할 수 없음

def solution(new_id):
  # 7단계 순차 처리 과정
  # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
  new_id = new_id.lower()

  # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
  copy_id = new_id
  new_id = ''
  for c in copy_id:
    if c.isdigit() or c.islower() or c in ['-','_','.']:
      new_id += c

  # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
  while '..' in new_id: 
    new_id = new_id.replace('..','.')

  # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
  if new_id and new_id[0] == '.':
    new_id = new_id[1:]
  if new_id and new_id[-1] == '.':
    new_id = new_id[:-1]
  
  # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
  if not new_id:
    new_id = 'a'

  # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
  # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
  if len(new_id) >= 16:
    new_id = new_id[:15]

  if new_id[-1] == '.':
    new_id = new_id[:-1]

  # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
  if len(new_id) <= 2:
    while len(new_id) < 3:
      new_id += new_id[-1]

  
  return new_id


new_id = "...!@BaT#*..y.abcdefghijklm"	
new_id = "z-+.^."
new_id = "=.="
new_id = "123_.def"
new_id = "abcdefghijklmn.p"

print(solution(new_id))


''' 
정규식 사용 풀이

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

'''