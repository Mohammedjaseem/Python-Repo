"""
Write an object oriented program to store and display the values of a 2D array
Program should contains 3 functions including the main function
main()
Declare an array
Call function getArray()
Call function displayArray()

"""
def main():
    getArray()
    displayArray()

def getArray():
    print("\nEnter the 1st Array elements: ")
    for i in range(limit):
        for j in range(limit):
            array1[i][j] = int(input("\nEnter the element: "))

def displayArray():
    limit = len(array1)
    print("\n Sum of array 1 and array 2")
    for i in range(limit):
        for j in range(limit):
            print(array1[i][j]," ",end=" ")
        print("\n")

limit = int(input("\nEnter the limit: "))
array1 = [[0 for x in range(limit)] for y in range(limit)]

main()