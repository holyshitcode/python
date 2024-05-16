sex = {
    '1' : 'man',
    '3' : 'man',
    '2' : 'woman',
    '4' : 'woman'
}

numbers=input("000000-0000000:")
sex_number=numbers[7]

if sex_number in  sex:
    print(f"당신의 성별은 {sex[sex_number]} 입니다.")
