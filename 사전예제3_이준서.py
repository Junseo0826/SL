'''
문제 분석 : 인치 입력받아 실수 변환후 inch에 저장한다.
           센티미터 : inch * 2.54
'''
# 1. 인치를 입력받아 실수로 변환후 inch에 저장한다.
inch = float(input('인치 입력 :'))
# 2. "00인치는 00센티미터 입니다."를 출력한다. (cm = inch*2.54)
print('{}인치는 {}센티미터 입니다.' .format(inch, inch*2.54))