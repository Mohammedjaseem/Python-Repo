
# need to fix error


#new user file creation
import json


def new_user(new_user,pincode):
    #To creat a new userfile
    filename= new_user + ".txt"
    file = open(filename, "w") 
    file.write('{ \n')
    file.write('"user_name_db": {},'.format(new_user))
    file.write('\n"Pin_db": {},'.format(pincode))
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

#balance fetch from user_db file
user_data_js = read_user_db("ayisha")
user_data = user_data_js
balance_amount = user_data_js.get("balance")







"""
new codes above
"""


# user dictionary

global user_list
user_list = {
  "jaseem": 2323,
  "murshid": 3434,
  "hammer" : 4545,
  "althaf": 5656,
  "althaf": 6666,
}

# global values
balance_amount = 0
global pin_status
pin_status = 0

# Funcation Declarations
def pinchecker(fnname):
    global pin_status
    global user_list
    try:
        global user_name
        user_name = input("\nEnter your user name: ")
    except:
        print("\nPlease enter a valid user name\n")
        pinchecker(fnname)

    #user db file check
    global user_data
    user_data_js = read_user_db(user_name)
    user_data = user_data_js
    name = user_data_js.get("user_name_db")
    print (name)
    pin_dic = (user_data.get("Pin_db"))
    print(pin_dic)
    #check ends here


    if name == user_name:
            print("\nWelcome {}".format(user_name))
            try:
             pin = int(input("\nEnter your pin: "))
            except:
                print("\nPlease enter a valid pin\n")
                pinchecker(fnname)

            pin_dic = (user_data.get("Pin_db"))
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
    global user_list
    global user_name
    global pin_status
    user_name = input("\nEnter your user name: ")
    if user_name in user_list:
        print("\nUser name already exists\n")
        add_user()
    else:
        pin = int(input("\nEnter your pin: "))
        if ((pin > 999) and (pin < 9999)):
             new_user(user_name,pin)
             print("\nUser added successfully\n")
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

print("\n Welcome to the ATM \n")

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
  