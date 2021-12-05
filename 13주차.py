#section_105.py

f = open('c:/파이썬 연습/myfile.txt', 'w')
poem = '''
살어리살어리 ㅁㄴ이럼니;ㅇ러ㅏ
ㅁㄴ이라ㅓㅁ니;ㅇ러ㅣ마;ㄴ얼
미;ㄴㅇ러;민어리;마넝ㄹ

살어리살어리
'''
f.close()
with open('c:/파이썬 연습/myfile.txt', 'w') as f:
      f.write(poem)


with open('c:/파이썬 연습/myfile.txt','r') as f:
     print('-----원본파일 -----')
     print(f.read())

poem1 ='''
    우러라 우러라
    우러우러
    우러라라라라
    '''

with open('c:/파이썬 연습/myfile.txt','a') as f:
    f.write(poem1)

with open('c:/파이썬 연습/myfile.txt','r') as f:
    print('----데이터 추가 ----')
    print(f.read())
