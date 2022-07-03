
from array import array

'''
Write a program to accept an array and display it on the console using functions
Program should contain 3 functions including main() function
main()
    Declare an array
    Call function getArray()
    Call function displayArray()

getArray()
    Get values to the array

displayArray()
    Display the array values

'''


def main():
    array1 = []
    getArray(array1)
    displayArray(array1)

def getArray (array1):
    array_size = int(input("Enter the size of the array: "))
    print("Enter the elements of the array: ")
    for i in range(array_size):
        array1.append(int(input()))
    return array1

def displayArray (array1):
    print("The elements of the array are: ")
    for i in range(len(array1)):
        print(array1[i]," ",end=" ")
    print("\n")


main()