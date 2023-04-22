# 1. 
id = input('아이디 :')
pas = input('패스워드 :')
if id == "admin" and pas == "pw1234":
    print('로그인 성공')
elif id != "admin" and pas == "pw1234":
    print('아이디가 틀렸습니다.')
elif id == "admin" and pas != "pw1234":
    print('패스워드가 틀렸습니다.')
else :
    print('아이디, 패스워드가 틀렸습니다.')