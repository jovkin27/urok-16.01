#import random
#str0=".,:;!_*-+()/#¤%&"
#str1 = '0123456789'
#str2 = 'qwertyuiopasdfghjklzxcvbnm'
#str3 = str2.upper()
#print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
#str4 = str0+str1+str2+str3
#print(str4)
#ls = list(str4)
#print(ls)
#random.shuffle(ls)
#print(ls)


login=["Jovkin","EcToGENt","Isedeaph","Gelsolit"]
password=["xfj8cne","3dcenwc","7xxfc6k","6b8p3qe"]
y=0

#for i in range (len(login)):
#    if login[y]==user:
#        print("Pass")
#    elif login[y]!=user: y+=1
#else:
#    print("You need to register")

#print("Tere tulemast")
from MyModule import authorisation
from MyModule import create
import datetime

while True:
    print("Do you want to register[1] or login[2] or Exit[3]")
    anw=int(input())
    if anw==3:
        print("Goodbye(")
        break
    elif anw==2:
        log=authorisation(input("Login: "),input("Password: "))
        print("Time",datetime.datetime.now())
        print("Do you want leave[1] or stay[2]")
        ques=int(input())
        if ques==1:
            break
        elif ques==2:
            ":)"
        else:
            "Error"
    elif anw==1:
        crt=create(input("Login:"),input("Password:"))
        #print("Create your Login")
        #user=input("Login: ")
        #login.append(user)
        #pasw=input("Password: ")
        #password.append(pasw)
        #print("You have been succesfully registered")
        #print("Try to log in")
       