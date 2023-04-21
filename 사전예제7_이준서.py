num = int(input('숫자 :'))
if num > 0:
    if num // 1000 >= 1:
        print('입력받은 정수는 네자리 수 이상입니다.')
    elif num // 100 >= 1:
        print('입력받은 정수는 세자리 수 입니다.')
    elif num // 10 >= 1:
        print('입력받은 정수는 두자리 수 입니다.')
    elif num // 1 >= 1:
        print('입력받은 정수는 한자리 수 입니다.')
else :
    if num // -1000 >= 1:
        print('입력받은 정수는 네자리 수 이상입니다.')
    elif num // -100 >= 1:
        print('입력받은 정수는 세자리 수 입니다.')
    elif num // -10 >= 1:
        print('입력받은 정수는 두자리 수 입니다.')
    elif num // -1 >= 1:
        print('입력받은 정수는 한자리 수 입니다.')