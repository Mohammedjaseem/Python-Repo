'''
Write a program to add to two dimensional arrays
Program should accept two 2D arrays and display its sum

'''

array_size = int(input("Enter the size of the array: "))
array1 = [[0 for x in range(array_size)] for y in range(array_size)] 
array2 = [[0 for x in range(array_size)] for y in range(array_size)]

print("Enter the elements of the 1st array: ")
for i in range(array_size):
    for j in range(array_size):
        array1[i][j] = int(input())

print("Enter the elements of the 2nd array: ")
for i in range(array_size):
    for j in range(array_size):
        array2[i][j] = int(input())

print("Sum of the two arrays: ")
for i in range(array_size):
    for j in range(array_size):
        print(array1[i][j]+array2[i][j]," ",end=" ")
    print()


