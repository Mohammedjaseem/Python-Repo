'''
Write a menu driven program to do the basic mathematical operations such as addition, subtraction, multiplication and division (hint: use if else ladder or switch)
Program should have 4 functions named addition(), subtraction(), multiplication() and division()
Should create a class object and call the appropriate function as user prefers in the main function

'''


def main(num1,num2):
    print("""Choose an option: 
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Exit """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add(num1,num2)
    elif choice == 2:
        sub(num1,num2)
    elif choice == 3:
        mul(num1,num2)
    elif choice == 4:
        div(num1,num2)
    elif choice == 5:
        exit()
    else:
        print("Invalid choice")
        main(num1,num2)

def add(num1,num2):
    print(num1,"+",num2,"=",num1+num2)
    print("\n")
    main(num1,num2)

def sub(num1,num2):
    print(num1,"-",num2,"=",num1-num2)
    print("\n")
    main(num1,num2)
def mul(num1,num2):
    print(num1,"*",num2,"=",num1*num2)
    print("\n")
    main(num1,num2)

def div(num1,num2):
    print(num1,"/",num2,"=",num1/num2)
    print("\n")
    main(num1,num2)


num1 =  int(input("Enter first number: "))
num2 =  int(input("Enter second number: "))
main(num1,num2)
    

    