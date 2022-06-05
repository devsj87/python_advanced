# 실습문제 2.4.1
# 리스트 내포를 사용해서 word_list에 들어 있는 문자열 중 첫 글자가 a인 것만 뽑아서 리스트로 만드세요
# 변경전 

word_list = ["apple", "watch", "apolo", "star", "abocado"]
# 리스트 내포 사용하기 전
list = []
for str in word_list:
  if str[0] == 'a':
    list.append(str)
print(list)

# 리스트 내포 사용 후
list2 = [str for str in word_list if str[0] == 'a']
print(list2)