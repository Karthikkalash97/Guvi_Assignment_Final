def valid_username(username):
    flag = True
    special = "#$%^&*"
    if '@' in username and "." in username:
        # ChecK Positions of @ and .
        for i in range(len(username)):
            if username[i] == "@":
                a_pos = i
            elif username[i] == ".":
                dot_pos = i
        if a_pos < dot_pos and dot_pos - a_pos != 1:
            flag = True
        else:
            flag = False


        for i in username:
            if i == " " or i in special:  #Check for special charecters and spaces other than @
                flag = False
                break
            elif username[0] in '123456789': #Check if username starts with a number
                flag = False
                break
            elif username[-3:] != 'com':
                flag = False
                break
    else:
        flag = False
    return flag

def valid_password(password):
    flag = True
    s,d,u,l = 0,0,0,0
    if len(password) > 5 and len(password) < 16:
        for i in password:
            if i.islower(): #Check For Lower Case
                l+=1
            elif i.isupper(): #Check for Upper Case
                u += 1
            elif i.isdigit(): #Check for numbers
                d += 1
            elif i in "!@#$%^&*": #Check for special charecters
                s+= 1

    if (l>=1 and u >=1 and s>=1 and d >=1 and l+u+d+s == len(password)):
        return True
    else:
        return False

def checkuser(username):
    with open("User.txt",'r') as f:
        if username + ":" in f.read():
            return True
        else:
            return False

def try_again():
    answer= input("Would you like to continue to login?\n1.Y for Yes\n2.N to exit program\n")
    if answer == "Y" or answer == 'y':
        login()
    elif (answer == "N" or answer == 'n'):
        print("Thank you for visiting!")
    else:
        print("Invalid Entry Please try again!")
        try_again()


def Register():
    username = input("Please enter usernname :").lower()
    password = input("Please enter password :")
    c_password = input('Please re-enter password :')
    with open("User.txt", 'r') as database:
        if password == c_password:
            if valid_password(password):
                if valid_username(username):
                    entry = username+":"+" "+password
                    if checkuser(username) == False:
                        f = open("User.txt",'a')
                        f.write(entry+'\n')
                        f.close()
                        print("Registration Done!")
                        try_again()



                    else:
                        print("Username already exists\nPlease try again")
                        Register()
                else:
                    print("Invalid Username, please try again!")
                    Register()
            else:
                print('Invalid Password , Please try again!')
                Register()
        else:
            print("Passwords dont match!. Please try again")
            Register()


def forgot_password():
    u = input("Please enter username:")
    flag = False
    with open('User.txt', 'r') as file:
        for line in file.readlines():
            if line.split()[0] == (u +":"):
                print("Username Found!")
                pswd = line.split()[1]
                print("Password = ", pswd)
                print("Try Logging in again")
                login()
                flag = True
                break

        if flag == False:

            print('Username not found!!')
            ch = input(
                "1. PLease enter 1 to register new user\n2. Any other charecter to exit the program\nChoice:")
            if ch == '1':
                Register()

def login():
    username = input("Please enter username : ")
    password = input("Please enter password : ")

    if checkuser(username):
        flag = False
        f = open("User.txt",'r')
        for line in f.readlines():
            if line.split()[0]== username+":" and line.split()[1] == password:
                print("Welcome",username)
                flag = True
                break
        if flag == False:
            print("Incorrect Password")
            c = input("Enter Y to try again\n2. Enter 2 to retrive password\n3. Enter any other key to exit:")
            if c == "Y":
                login()
            elif c == "2":
                forgot_password()
            else:
                print("Thank you for using the program!")

    else:
        print("Username does not exist! Please try again")
        login()

def admin_login():
    username = input("Please enter username : ")
    password = input("Please enter password : ")

    if check_admin(username):
        flag = False
        f = open("Admin.txt", 'r')
        for line in f.readlines():
            if line.split()[0] == username + ":" and line.split()[1] == password:
                print("Welcome", username)
                flag = True
                break

        if flag == False:
            print("Incorrect Password")
            c = input("Enter Y to try again or N to exit:")
            if c == "Y":
                admin_login()
        elif flag == True:
            admin_operations()
    else:
        print("Username does not exist! Please try again")
        admin_login()


def Register2():
    username = input("Please enter usernname :").lower()
    password = input("Please enter password :")
    c_password = input('Please re-enter password :')
    with open("User.txt", 'r') as database:
        if password == c_password:
            if valid_password(password):
                if valid_username(username):
                    entry = username+":"+" "+password
                    if checkuser(username) == False:
                        f = open("User.txt",'a')
                        f.write(entry+'\n')
                        f.close()
                        print("Registration Done!")
                        admin_operations()



                    else:
                        print("Username already exists\nPlease try again")
                        Register2()
                else:
                    print("Invalid Username, please try again!")
                    Register2()
            else:
                print('Invalid Password , Please try again!')
                Register2()
        else:
            print("Passwords dont match!. Please try again")
            Register2()

def check_admin(username):
    with open("Admin.txt",'r') as f:
        if username + ":" in f.read():
            return True
        else:
            return False

def admin_registration():
    username = input("Please enter usernname :").lower()
    password = input("Please enter password :")
    c_password = input('Please re-enter password :')
    with open("Admin.txt", 'r') as database:
        if password == c_password:
            if valid_password(password):
                if valid_username(username):
                    entry = username + ":" + " " + password
                    if check_admin(username) == False:
                        f = open("Admin.txt", 'a')
                        f.write(entry + '\n')
                        f.close()
                        print("Registration Done!")
                        admin_operations()



                    else:
                        print("Username already exists\nPlease try again")
                        admin_registration()
                else:
                    print("Invalid Username, please try again!")
                    admin_registration()
            else:
                print('Invalid Password , Please try again!')
                admin_registration()
        else:
            print("Passwords dont match!. Please try again")
            admin_registration()


def admin_operations():
    operation = int(input(
        "Please select an opeation:\n1.Create new user\n2.Delete existing user\n3.Create new admin\n4.Exit program\nopeation:"))

    if operation == 1:
        Register2()
    elif operation == 2:
        delete_user()
    elif operation == 3:
        admin_registration()
    elif operation == 4:
        print("Thank you, Have a nice day!")
    else:
        print("Invalid input please try again!")


        admin_operations()


def delete_user():
    username = input("Please enter the username of the account you would like to delete :")
    with open("User.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line.split()[0] != username +":":
                f.write(line)
        f.truncate()
        print("Done!")
        admin_operations()

def choice():
    print("********** Welcome to  GUVI DataNerds Database login system **********")
    ch = int(input("Please select an operation\n1.Register : Please enter 1\n2.Login: Please enter 2\n3.Admin Login: Please enter 3\nChoice:"))
    if ch == 1:
        Register()
    elif ch == 2:
        login()
    elif ch == 3:
        admin_login()
    else:
        print("Invalid entry please try again")
        choice()

choice()