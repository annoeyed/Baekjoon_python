# 1157 단어 공부
'''
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
첫째 줄에 알파벳 대소문자로 된 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

from collections import Counter

word = input().upper()     # 입력 단어를 모두 대문자로 변환
counter = Counter(word)    # 각 문자 빈도수 세기
most_common = counter.most_common()  # 빈도수가 많은 순서대로 정렬된 리스트

if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print('?')             # 가장 많은 빈도수가 동률이면 '?'
else:
    print(most_common[0][0])   # 아니면 가장 많이 나온 알파벳 출력
