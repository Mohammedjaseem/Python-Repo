# Write a program to multiply the adjacent values of an array and store it in an another array

def get_array():
    arraySize = int(input("\nEnter the size of the array: "))
    arrayz = []
    print("\nEnter the elements of the array: ")
    for i in range(0,arraySize):
        arrayz.append(int(input()))
    return arrayz
    
def multi_adj_elem(arrayz):
    result_array = []
    for i in range(0,len(arrayz)):
            if(i+1 < len(arrayz)):
                new_element = arrayz[i] * arrayz[i+1]
                result_array.append(new_element)
            else:
                break
    return result_array

def display_new_array(result_array):
    print("\nThe Multiple of adj elememts: ")
    for i in range(len(result_array)):
        print(result_array[i]," ",end=" ")

def Multiply_adj_elements():
    display_new_array(multi_adj_elem(get_array()))

Multiply_adj_elements()