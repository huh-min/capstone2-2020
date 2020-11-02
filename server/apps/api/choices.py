# This file saves constant list for choice fields options.
# 알파벳 순으로 정렬.
import json

GENDER_CHOICES = [
    ('M', 'M'),
    ('W', 'W'),
]

with open('apps/api/locations/data.json') as json_file:
    data = json.load(json_file)
    
LOCATION_CHOICES = []
for row in data:
    LOCATION_CHOICES.append((int(row), data[row]['full_address']))

LOWER_CATEGORY_CHOICES = [
    ('반팔티셔츠', '반팔티셔츠'),
    ('긴팔티셔츠', '긴팔티셔츠'),
    ('반팔셔츠', '반팔셔츠'),
    ('긴팔셔츠', '긴팔셔츠'),
    ('맨투맨', '맨투맨'),
    ('터틀넥', '터틀넥'),
    ('후드티', '후드티'),
    ('니트', '니트'),
    ('블라우스', '블라우스'),
    ('끈나시', '끈나시'),
    ('민소매', '민소매'),
    ('반바지', '반바지'),
    ('핫팬츠', '핫팬츠'),
    ('슬랙스', '슬랙스'),
    ('청바지', '청바지'),
    ('골덴바지', '골덴바지'),
    ('트레이닝바지', '트레이닝바지'),
    ('미니스커트', '미니스커트'),
    ('롱스커트', '롱스커트'),
    ('블레이져', '블레이져'),
    ('숏패딩', '숏패딩'),
    ('조끼패딩', '조끼패딩'),
    ('롱패딩', '롱패딩'),
    ('야구점퍼', '야구점퍼'),
    ('항공점퍼', '항공점퍼'),
    ('바람막이', '바람막이'),
    ('야상', '야상'),
    ('무스탕', '무스탕'),
    ('코트', '코트'),
    ('트랙탑', '트랙탑'),
    ('가죽자켓', '가죽자켓'),
    ('청자켓', '청자켓'),
    ('가디건', '가디건'),
    ('원피스', '원피스')
]

REVIEW_CHOICES = [
    (1, '춥다'),
    (2, '조금춥다'),
    (3, '좋다'),
    (4, '조금덥다'),
    (5, '덥다'),
]

STYLE_CHOICES = [
    ('심플', '심플'),
    ('스트릿', '스트릿'),
    ('정장', '정장'),
    ('데이트', '데이트'),
    ('화려', '화려'),
]

TIME_CHOICES = [
    (2, 2),
    (5, 5),
    (8, 8),
    (11, 11), 
    (14, 14),
    (17, 17),
    (20, 20),
    (23, 23),
]

UPPER_CATEGORY_CHOICES = [
    ('하의', '하의'),
    ('원피스', '원피스'),
    ('아우터', '아우터'),
    ('치마', '치마'),
    ('상의', '상의'),
]

WEATHER_TYPE_CHOICES = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
]
