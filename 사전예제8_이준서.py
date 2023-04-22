# 1. 년도를 정수로 변환하여 년도 변수 year에 저장한다.
year = int(input('년도 입력 :'))
# 2. 만약 year % 4 == 0이면
if year % 4 == 0:
#   1) 만약 year % 400 == 0이면
#   1-1) "year년은 윤년입니다."를 출력한다.
    if year % 400 == 0:
        print('{}년은 윤년입니다.' .format(year))
#   2) 아니고 만약 year % 100 == 0이면
#   2-1) "year년은 윤년이 아닙니다."를 출력한다.
    elif year % 100 == 0:
        print('{}년은 윤년이 아닙니다.' .format(year))
#   3) 아니면
#   3-1) "year년은 윤년입니다."를 출력한다.
    else :
        print('{}년은 윤년입니다.' .format(year))
# 3. 아니면
#   1) "year년은 윤년이 아닙니다."를 출력한다. 
else :
    print('{}년은 윤년이 아닙니다.' .format(year))