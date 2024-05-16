regions = {
    '00' : 'seoul',
    '01' : 'seoul',
    '02' : 'seoul',
    '03' : 'seoul',
    '04' : 'seoul',
    '05' : 'seoul',
    '06' : 'seoul',
    '07' : 'seoul',
    '08' : 'seoul',
    '09' : 'busan',
    '10' : 'busan',
    '11' : 'busan',
    '12' : 'busan',
}

numbers=input("000000-0000000:")
region_number=numbers[8]+numbers[9]

if region_number in  regions:
    if regions[region_number] == "seoul":
        print(f"당신의 지역은 {regions[region_number]} 입니다.")
    else:
        pass
else:
    print("서울이 아닙니다.")
