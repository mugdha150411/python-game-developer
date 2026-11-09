d={"mary":"mary@1234","emily":"567emily_3","paul":"009paul23//","john":"john@829","freya":"12_freya@456"}
username=input("enter your username: ")
if username not in d:
        print("you are not a valid user of this system")
else:
    print("you are a valid user of this system")
    password=input("enter your password: ")
    if password!=d[username]:
        print("the password is invalid!")
    elif password==d[username]:
        print("you are now logged into the system!")
