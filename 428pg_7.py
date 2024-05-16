from datetime import datetime, timedelta

# 오늘 날짜 가져오기
today = datetime.now().date()

# 5일 전 날짜 계산
five_days_ago = today - timedelta(days=5)

# 오늘부터 5일 전까지의 날짜를 하루씩 출력
current_date = today
while current_date >= five_days_ago:
    print(current_date)
    current_date -= timedelta(days=1)
