def main():
    getArray()
    addArray()
    display()

def getArray():
    print("\nEnter the 1st Array elements: ")
    for i in range(limit):
        for j in range(limit):
            array1[i][j] = int(input("\nEnter the element: "))
    
    print("\nEnter the 2nd Array elements: ")
    for i in range(limit):
        for j in range(limit):
            array2[i][j] = int(input("\nEnter the element: "))

def addArray():
    limit = len(array1)
    arraynew = [[0 for x in range(limit)] for y in range(limit)]
    for i in range(limit):
        for j in range(limit):
            arraynew[i][j] = array2[i][j] + array1[i][j]
    return arraynew

def display():
    limit = len(addArray())
    arraynew = addArray()
    print("\n Sum of array 1 and array 2")
    for i in range(limit):
        for j in range(limit):
            print(arraynew[i][j]," ",end=" ")
        print("\n")

# User Input 
limit=int(input("\nEnter the limit: "))
array1 = [[0 for x in range(limit)] for y in range(limit)]
array2 = [[0 for x in range(limit)] for y in range(limit)]

# Calling the main function
main()

