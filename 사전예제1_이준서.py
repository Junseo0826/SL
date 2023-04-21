# 1. 어린이 인원을 정수로 변환하여 어린이 인원 변수 child에 저장한다.
child = int(input('어린이 인원 :'))
# 2. 보통 인원을 정수로 변환하여 보통 인원 변수 adult에 저장한다.
adult = int(input('보통 인원 :'))
# 3. 경로우대 인원을 정수로 변환하여 경로우대 인원 변수 senior에 저장한다.
senior = int(input('경로우대 인원 :'))
# 4. 총 요금 = child * 5000 + adult * 10000 + senior * 7000
total = child * 5000 + adult * 10000 + senior * 7000
# 5. 만약 child + adult + senior >= 10이면
#   1) "어린이 00명, 어른 00명, 경로우대 00명의 총 요금은 00원입니다." (총요금에 0.8을 곱하여) 를 출력한다.
if child + adult + senior >= 10:
    print('어린이{}명, 어른{}명, 경로우대{}명의 총 요금은 {}원입니다.' .format(child,adult,senior,total*0.8))
# 6. 아니면
#   1) "어린이 00명, 어른 00명, 경로우대 00명의 총 요금은 00원입니다."를 출력한다.
else :
    print('어린이{}명, 어른{}명, 경로우대{}명의 총 요금은 {}원입니다.' .format(child,adult,senior,total))