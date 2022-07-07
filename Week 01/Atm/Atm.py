# user dic

global user_list

user_list = {
  "jaseem": 2323,
  "murshid": 3434,
  "hammer" : 4545,
  "althaf": 5656,
  "althaf": 6666,
}


# global values
global balance_amount 
balance_amount = 0
global pin_status
pin_status = 0

# Funcation Declarations
def pinchecker(fnname):
    global pin_status
    global user_list
    try:
        user_name = input("\nEnter your user name: ")
    except:
        print("\nPlease enter a valid user name\n")
        pinchecker(fnname)
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
                print ("pin_status:", pin_status)
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
                withdraw()
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
        

# Atm Start from here

print("/n Welcome to the ATM /n")

def choice():
    print("""Please Choose an option:
    1. Check Balance
    2. Withdraw
    3. Deposit
    4. Exit""")
    try:
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            balance()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            deposite()
        elif choice == 4:
            print("\nThank you for using our ATM\n")
            exit()
    except:
        print("\nPlease enter a valid choice\n")
    


while True:
    choice()