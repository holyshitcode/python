middle=int(input("중간고사:"))
final=int(input("기말고사:"))

sum= middle+final
avg= sum/2

with open("score.txt",'w') as f1:
    result=f"{middle}\t\t{final}\t\t{sum}\t{avg}\n"
    line=f"{'*'*60}\n"
    f1.write("이름(학번) : 김준영(202411340)\n")
    f1.write(line)
    f1.write(f"중간고사\t기말고사\t 총점\t 평균\n")
    f1.write(line)
    f1.write(result)
    f1.write(line)
    f1.close
with open("score.txt",'r') as f2:
    record=f2.read()
    print(record)