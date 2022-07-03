# Write a program to find the sum of all the odd numbers for a given limit
# Program should accept an input as limit from the user and display the sum of all the odd numbers within that limit
# For example if the input limit is 10 then the result is 1+3+5+7+9 = 25


limit = int(input("Enter Limit: "))
sum = 0
for i in range(1,limit+1):
    if(i%2!=0):
        sum = sum + i
print("Sum of odd numbers upto",limit ,"is ", sum)
