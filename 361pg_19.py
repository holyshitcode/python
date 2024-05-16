#12자리의 각 숫자에 2,3,4,5,6,7,8,9,2,3,4,5 를 차례로 곱한뒤 그값을 전부더해서 11로 나눈후 나머지를 구한후 11에서 이 나머지를 뺀값이 마지막숫자

register_num=input("공백없이입력")
flag=2
sum_num=[]
for j in range(12):
   result=int(register_num[j])*flag
   print(result)
   sum_num.append(result)
   if flag >8:
      flag= 2
   else:
      flag+=1
print(sum_num)
valid_num=sum(sum_num)
final_num=11-valid_num%11

if int(register_num[12])==int(final_num):
   print("valid information")
else:
   print("invalid information")
