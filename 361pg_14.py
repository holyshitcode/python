num_list=[]
for i in range(1,21):
    num_list.append(i)

num=1

while True:
    count=0
    for i in range(20):
        result=num%num_list[i]
        if result ==0:
            count+=1
        else:
            continue
    if count==20:
        print(num)
        break
    else:
        print(count)
        num+=1

    


    