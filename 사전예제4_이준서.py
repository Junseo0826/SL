'''
문제 분석 : 시급을 입력받는다.
           노동시간을 입력받는다.
'''
wage = int(input('시급 입력 :'))
time = int(input('노동시간 입력 :'))
print('시급 {}원으로 {}으로 일했으므로 수당은 {}원입니다.' .format(wage,time,wage*time))