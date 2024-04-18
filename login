right_id="junyeong"
right_pw="junjun"

def checkid():
    count=0
    id=input("enter your id:")
    pw=input("enter your password:")
    while count<2:
        if id==right_id and pw==right_pw:
            print("successfully loggined")
            break
        else:
            count+=1
            print("please try again")
            id=input("enter your id:")
            pw=input("enter your password:")
    print("unexpected try detected. program will be exited")        
    return None

checkid()
        
