exchange = {
    'usd': 1320,
    'jpy': 950,
    'cny': 182
}

money = [13, 200, 13]

# 각 통화를 한화로 환산
total = 0

# 달러 환산
total += money[0] * exchange['usd']

# 엔화 환산
total += money[1] * exchange['jpy']

# 위안 환산
total += money[2] * exchange['cny']

# 결과 출력
print("철수가 가지고 있는 돈의 원화 가치는", total, "원 입니다.")