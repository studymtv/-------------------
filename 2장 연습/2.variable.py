monday_end_price = 10000 - (10000 * 0.3)
tuesday_end_price = monday_end_price - (monday_end_price * 0.3)
print(tuesday_end_price)

x = 100
y = 100
print(id(x),id(y))

x = 10000
y = 10000
print(id(x),id(y))

mystring  = 'hello world'
print(mystring)

mystring  = 'hello world'
print(len(mystring))
print(mystring[0:11])
print(mystring[6:-1])


my_jusik = "naver daum"
print(my_jusik.split(' '))
print(my_jusik.split(' ')[0])
print(my_jusik.split(' ')[1])


daum = "Daum"
kakao = "KAKAO"
print(daum + ' ' + kakao)
