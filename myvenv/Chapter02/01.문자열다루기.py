# 1. replace
# 문자열 교체
a = "오늘 날씨는 흐림입니다.".replace("흐림","맑음")
print(a)

# 2. find
# 문자열 찾기

b = "Hello World".find("World")
print(b)

# 3. split
# 문자열 분리
c = "나이키 신발 265 X1212 78000".split()
print(c)
d = "나이키:신발:265:X1212:78000".split(":")
print(d)

# 4. strip
# 문자열 공백 제거
e = '         Yaeh       '.lstrip()
print(e)
f = '         Yaeh       '.rstrip()
print(f)
g = '         Yaeh       '.strip()
print(g)
