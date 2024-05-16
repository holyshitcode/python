telecom = {
    '011' : "skt",
    '016' : "kt",
    '019' : "lgu",
    '010' : "unkown"
}

phone_num=input("-로 이어주세요:")
numbers=[]
numbers=phone_num.split("-")

if numbers[0] in telecom:
    print(f"당신은{telecom[numbers[0]]} 사용자입니다")
else: 
    print("등록되지않았습니다")
