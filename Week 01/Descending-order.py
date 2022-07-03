'''
 Write a program to sort an array in descending order
Program should accept and array, sort the array values in descending order and display it

'''

Array_Size = int(input("Enter the size of the array: "))
Array = []

print("Enter the elements of the array: ")
for i in range(Array_Size):
    Array.append(int(input()))

# Sorting of array
Array.sort(reverse=True)

# Displaying the array
print("The elements of the array are: ")
for i in range(Array_Size):
    print(Array[i]," ",end=" ")
