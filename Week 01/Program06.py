# Using the ‘switch case’ write a program to accept an input number from the user and output the day

num = int(input("Enter the day of the week: "))
if(num == 1):
    print("Monday")
elif(num == 2):
    print("Tuesday")
elif(num == 3):
    print("Wednesday")
elif(num == 4):
    print("Thursday")
elif(num == 5):
    print("Friday")
elif(num == 6):
    print("Saturday")
elif(num == 7):
    print("Sunday")
else:
    print("Invalid Input")
