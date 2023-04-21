money = int(input('돈 :'))
change = money - 350
# 나머지 650
change01 = change % 1000
change1 = change // 1000
# 나머지 150
change02 = change01 % 500
change2 = change01 // 500
change03 = change02 % 100
change3 = change02 // 100
change04 = change03 % 50
change4 = change03 // 50
change05 = change04 % 10
change5 = change04 // 10
print('천원짜리 지폐 {}개, 오백원짜리 동전 {}개, 백원짜리 동전 {}개, 오십원짜리 동전 {}개, 십원짜리 동전{}개 입니다.' .format(change1, change2,change3,change4,change5))