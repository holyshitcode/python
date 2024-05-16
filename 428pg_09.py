import random
lotto=[]
for result in random.sample(range(1,46),6):
    lotto.append(result)

print(f"행운의 당첨번호는 ={lotto}")

