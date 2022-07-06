limit = int(input("Enter the limit: "))
num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2
print("Number is",num,"and square",nearest_square)