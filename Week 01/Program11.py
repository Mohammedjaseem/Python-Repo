# Write a program to find the number of even numbers in an array
# Program should accept an array and display the number of even numbers contained in that array

Array_size = int(input("Enter the size of the array: "))
Array = []
print("Enter the elements of the array: ")
for i in range(Array_size):
    Array.append(int(input()))

print("The elements of the array are: ")
for i in range(Array_size):
    print(Array[i]," ",end=" ")
print("\n")

even_count = 0
for i in range(Array_size):
    if Array[i]%2 == 0:
        even_count += 1
        
print("The number of even numbers in the array are: ",even_count)