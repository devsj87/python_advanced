# 실습문제 2.6.1
# 지도 어플리케이션에서 소요시간ㅇ들 크롤링 하였더니 문자열 데이터 였다. 소요시간을 비교하기 위해 시간을 모두 분으로 바꾸려고 한다.
# 다음과 같이 시간이 입력되면 분으로 바꾸어 주는 프로그램을 작성해보자

time = input(">>>> ")
sum = 0

if time.find('시간') == -1 :
  # 분만 있는경우
  result = int(time.split('분')[0])
  sum += result
else:
  if time.find('분') == -1:
    # 시간만 있는경우
    result = int(time.split('시간')[0]) * 60
    sum += result
    
  else:
    # 시간 과 분이 있는경우
    sub = time.split('시간')
    result = int(sub[0]) * 60 + int(sub[1].split('분')[0])
    sum += result

print(sum)
