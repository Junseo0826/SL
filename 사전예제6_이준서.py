com = int(input('컴퓨터 과목 점수 입력 :'))
eng = int(input('영어 과목 점수 입력 :'))
if com >= 95:
    print('합격입니다.')
elif eng >= 95:
    print('합격입니다.')
elif com + eng >= 170:
    print('합격입니다.')
else :
    print('불합격입니다.')