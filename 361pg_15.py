# 환율 딕셔너리 정의
exchange_rates = {
    "dollar": 1135.50,  # 1 달러 = 1135.50 원
    "en": 10.60,        # 1 엔 = 10.60 원
    "euro": 1325.50,    # 1 유로 = 1325.50 원
    "wian": 0.95        # 1 위안 = 0.95 원
}

# 입력 받기
user_input = input("금액과 통화를 입력하세요 (예: 100 dollar 200en 300euro 400wian): ")

# 입력을 공백을 기준으로 분리하여 리스트에 저장
input_list = user_input.split()

# 딕셔너리에 환율 적용하여 원화로 환전
result = 0
for i in range(0, len(input_list), 2):
    amount = float(input_list[i])  # 금액은 실수형으로 변환
    currency = input_list[i + 1]
    if currency in exchange_rates:
        result += amount * exchange_rates[currency]

# 결과 출력
print("원화로 환전한 금액:", result, "원")