'''
# 1. 다음 문구를 공백으로 구분하여 리스트에 저장한 후, 인덱스와 단어를 이용해서 딕셔너리에 저장해보자

pyThon = '파이썬은 1991년 네덜란드계 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, ' \
         '플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑 대화형 언어이다. ' \
         '파이썬이라는 이름은 귀도가 좋아하는 코미디인〈Monty Python\'s Flying Circus〉에서 따온 것이다.'

temList = pyThon.split()
print(temList)

dic = {}
for idx, str in enumerate(temList):
    dic[idx] = str


print(dic)
'''

# 2. 다음 문장에서 비속어를 찾고 비속어를 표준어로 변경하는 프로그램을 만들어보자
# 혼자하기 실패

str = '강도는 서로 쪼개다, 짭새를 보고 빠르게 따돌리며 먹튀했다.'

words = {'꺼지다': '가다', '쩔다': '엄청나다', '짭새': '경찰관',
         '꼽사리': '중간에 낀 사람', '먹튀': '먹고 도망',
         '지린다': '겁을 먹다', '쪼개다': '웃다',
         '뒷담 까다': '험담하다'}

# temList = str.split()  이번에는 이렇게 하는게 아니었음

keys = list(words.keys())

for key in keys:
    if key in str:
        print('key : {}'.format(key))
        print('words[{}] : {}'.format(key, words[key]))
        str = str.replace(key, words[key])

print(str)