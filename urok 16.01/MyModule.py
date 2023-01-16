login=["Jovkin","EcToGENt","Isedeaph","Gelsolit"]
password=["xfj8cne","3dcenwc","7xxfc6k","6b8p3qe"]

def authorisation(log:str,pas:str):
    """
    param:list log
    param:list pas
    """
    while log==str(log):
        if log in login:
            login.append(log)
            if pas in password:
                password.append(pas)
                print("Pass")
                print(f"Tere Tulemast {log}")
                break
            elif pas not in password:
                print("wrong password")
                pas=input("Password: ")
        elif log not in login:
            print("wrong login")
            log=input("Login: ")


def create(log:str,pas:str):
    """
    param: str log Login
    param: str pas Password
    :rtype: list append to list
    """
    login.append(log)
    while True:
        if len(pas)<10:
            print("Weak password,Try Again")
            pas=input("Password:")
        elif len(pas)>=10:
            password.append(pas)
            print("You sucessfuly registered")
            return log,pas
    #while len(pas)<10:
    #    print("Weak password")
    #    if len(pas)>=10:
    #        password.append(pas)
    #        print("You sucessfuly registered")
    #        return log,pas
    #    else:
    #        break