jumin = input("주민번호 13자리를 입력하세요:")
x = [2,3,4,5,6,7,8,9,2,3,4,5] #2에서 각자리에 곱하여야함
y = 0

for i in range(12) :
    sum = int(jumin[i] * x[i])
    y += sum #jumin과 x를 곱한 값을 더하여 y값에 추가하기

x = (11 - (y % 11)) % 10 # y를 11로 나눈후 11에서 나머지 결과값을 뺴줍니다.

if int(jumin[-1]) == x:
    print("주민번호",jumin[0:6],"-",jumin[6:13],"는 맞습니다.")
else :
    print("주민번호",jumin[0:6],"-",jumin[6:13],"는 맞지 않습니다.")