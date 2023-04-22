# 1. 년도를 정수로 변환하여 년도 변수 year에 저장한다.
year = int(input('년도 입력 :'))
# 2. 만약 year % 12 == 0이면
#   1) "year년은 원숭이띠입니다."를 출력한다.
if year % 12 == 0:
    print('{}년은 원숭이띠입니다.' .format(year))
# 3. 아니고 만약 year % 12 == 1이면
#   1) "year년은 닭띠입니다."를 출력한다.
elif year % 12 == 1:
    print('{}년은 닭띠입니다.' .format(year))
# 4. 아니고 만약 year % 12 == 2이면
#   1) "year년은 개띠입니다."를 출력한다.
elif year % 12 == 2:
    print('{}년은 개띠입니다.' .format(year))
# 5. 아니고 만약 year % 12 == 3이면
#   1) "year년은 돼지띠입니다."를 출력한다.
elif year % 12 == 3:
    print('{}년은 돼지띠입니다.' .format(year))
# 6. 아니고 만약 year % 12 == 4이면
#   1) "year년은 쥐띠입니다."를 출력한다.
elif year % 12 == 4:
    print('{}년은 쥐띠입니다.' .format(year))
# 7. 아니고 만약 year % 12 == 5이면
#   1) "year년은 소띠입니다."를 출력한다.
elif year % 12 == 5:
    print('{}년은 소띠입니다.' .format(year))
# 8. 아니고 만약 year % 12 == 6이면
#   1) "year년은 범띠입니다."를 출력한다.
elif year % 12 == 6:
    print('{}년은 범띠입니다.' .format(year))
# 9. 아니고 만약 year % 12 == 7이면
#   1) "year년은 토끼띠입니다."를 출력한다.
elif year % 12 == 7:
    print('{}년은 토끼띠입니다.' .format(year))
# 10. 아니고 만약 year % 12 == 8이면
#   1) "year년은 용띠입니다."를 출력한다.
elif year % 12 == 8:
    print('{}년은 용띠입니다.' .format(year))
# 11. 아니고 만약 year % 12 == 9이면
#   1) "year년은 뱀띠입니다."를 출력한다.
elif year % 12 == 9:
    print('{}년은 뱀띠입니다.' .format(year))
# 12. 아니고 만약 year % 12 == 10이면
#   1) "year년은 말띠입니다."를 출력한다.
elif year % 12 == 10:
    print('{}년은 말띠입니다.' .format(year))
# 13. 아니면
#   1) "year년은 양띠입니다."를 출력한다.
else :
    print('{}년은 양띠입니다.' .format(year))