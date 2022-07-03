'''
Write a program to interchange the values of two arrays.
Program should accept an array from the user, swap the values of two arrays and display it on the console

'''

array_size = int(input("Enter the size of the array: "))
print("Enter the elements of the array 1: ")

# Accepting the elements of the array1
array1 = []
for i in range(array_size):
    array1.append(int(input()))
print("Enter the elements of the array 2: ")

# Accepting the elements of the array2
array2 = []
for i in range(array_size):
    array2.append(int(input()))

# Swapping of array elements
for i in range(array_size):
    temp = array1[i]
    array1[i] = array2[i]
    array2[i] = temp

# Printing the array after swapping

print("Array 1 after swapping: ")
for i in range(array_size):
    print(array1[i]," ",end=" ")
print("\n")

print("Array 2 after swapping: ")
for i in range(array_size):
    print(array2[i]," ",end=" ")
print("\n")

