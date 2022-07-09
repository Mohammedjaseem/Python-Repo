import os.path
import json

# new file for new user
def new_user(new_user,pincode):
    #To creat a new userfile
    filename= new_user + ".txt"
    file = open(filename, "w") 
    file.write("user_db = { \n")
    file.write('"{}": {},'.format(new_user,pincode))
    file.write('\n"balance": 0\n}')
    file.close() 
    print("New user",new_user,"created")

#read user Db from Db file
def read_user_db(new_user):
    with open(new_user + ".txt") as f:
        global user_data
        user_data = f.read()
        user_data_js = json.loads(user_data)
        return user_data_js

# global values
global balance_amount 
global user_data
user_data_js = read_user_db("jaseem")
user_data = user_data_js
balance_amount = user_data_js.get("balance")
print(balance_amount)
pin_status = 0

# Funcation Declarations
def pinchecker(fnname):
    global pin_status
    try:
        global user_name
        user_name = input("\nEnter your user name: ")
        return user_name
    except:
        print("\nPlease enter a valid user name\n")
        pinchecker(fnname)

    global user_data
    user_list = open(user_name+".txt", "r")
    user_name = user_list.get()
    if user_name in user_list:
            print("\nWelcome {}".format(user_name))
            try:
             pin = int(input("\nEnter your pin: "))
            except:
                print("\nPlease enter a valid pin\n")
                pinchecker(fnname)

            pin_dic = (user_list.get(user_name))
            if pin == pin_dic:
                global pin_status
                pin_status = 1
                print ("Account Verified")
            else:
                print("\nWrong pin\n")
                pinchecker(fnname)
    else:
        print("\nUser Not Found!\n")
        pinchecker(fnname)
    
    back_functio = fnname
    back_functio()


def deposite():
    global balance_amount
    global pin_status
    if pin_status == 1:
        amount = int(input("\nEnter the amount to be deposited: "))
        if(amount >0):
            balance_amount += amount
            print("\nYour balance is:", balance_amount)
            choice()
        else:
            print("\nPlease enter a valid amount\n")
            deposite()
    pinchecker(deposite)

def balance():
    global balance_amount
    global pin_status
    
    if pin_status == 1:
         print("\nYour balance is:", balance_amount)
         print("\nThank you for using our ATM\n")
         choice()
    pinchecker(balance)

def withdraw():
    global balance_amount
    global pin_status
    if pin_status == 1:
        amount = int(input("\nEnter the amount to be withdrawn: "))
        if(amount >0):
            if (amount > balance_amount ):
                print("\nInsufficient balance\n")
                choice() 
            else:
                balance_amount -= amount
                print("Withdrawal successful :{}".format(amount))
                print("Your balance is:", balance_amount)
                print("\nThank you for using our ATM\n")
                choice()   
        else:
            print("\nPlease enter a valid amount\n")
            withdraw() 
    else:
        pinchecker(withdraw)  

def add_user():
    print("\nWelcome to the new user registration\n")
    global name
    global pin_status
    name = input("\nEnter your user name: ")
    file_exists = os.path.exists(name+".txt")
    if file_exists:
        print("\nUser name already exists\n")
        add_user()
    else:
        user_list = open(name+".txt", "w")
        pin = int(input("\nEnter your pin: "))
        if ((pin > 999) and (pin < 9999)):
             new_user(name,pin)
             choice()

def change_pin():
    global user_list
    global user_name
    global pin_status
    if pin_status == 1:
        new_pin = int(input("\nEnter your new pin: "))
        if ((new_pin > 999) and (new_pin < 9999)):
            user_list[user_name] = new_pin
            print("\nPin changed successfully\n")
            print("your new pin is :",user_list[user_name],"\n")
            pin_status = 0
            choice()
            return pin_status
        else:
            print("\nPlease enter a valid pin\n")
            change_pin()
    else:
        pinchecker(change_pin)
        

# Atm Start from here

print("/n Welcome to the ATM /n")

def choice():
    print("""Please Choose an option:
    1. Check Balance
    2. Withdraw
    3. Deposit
    4. Change pin
    5. New User
    6. Exit""")
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        balance()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        deposite()
    elif choice == 4:
        change_pin()
    elif choice == 5:
        add_user()
    elif choice == 6:
        print("\nThank you for using our ATM\n")
        exit()
    else:
        print("\nPlease enter a valid choice\n")
        main()
    
def main():
    while True:
        choice()

main()

