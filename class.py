class student:
    def __init__(self,age,class_num):
        self.age = age
        self.class_num = class_num
        #self.showInfo()

    def showInfo(self):
        print(f"{self.age} your age")
        print(f"{self.class_num} your class number")



junyeong = student(20,1)
junyeong1 = student(22,1)
junyeong2 = student(20,1)

print(junyeong.age)
print(junyeong1.age)


