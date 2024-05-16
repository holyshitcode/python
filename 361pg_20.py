import random

choice = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f'
}

num = int(input("enter number what you want by 6: "))

input("press enter to show result!")
# 중복되지 않는 1부터 6까지의 숫자를 선택합니다.
for result in random.sample(range(1, 7), num):
    print(f"{choice[str(result)]}-{result}")
