year = int(input('년도 입력 :'))
if year % 4 == 0 or year % 400 == 0:
    print('윤년 입니다.')
elif year % 100 == 0:
    print('윤년이 아닙니다.')
else :
    print('윤년이 아닙니다.')