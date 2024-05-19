def get_avg():
    score=[]
    for i in range(4):
        lesson = int(input("input score:"))
        score.append(lesson)
    return sum(score)/4

print(get_avg())

