# Write a program to check whether a given number is prime or not
# Program should accept an input from the user and display whether the number is prime or not

num = int (input("Enter the number: "))
for i in range(1,num):
    if num%i == 0:
        flag=False
        break
    else:
        flag=True
if flag:
    print("The number",num,"is prime")
else:
    print("The number",num,"is not prime")