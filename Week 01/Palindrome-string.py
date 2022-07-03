'''
Write a program to identify whether a string is a palindrome or not
A string is a palindrome if it reads the same backward or forward eg: MALAYALAM
'''
wordz = input("Enter the word: ")
lenght = len(wordz)
for i in range(lenght):
    if(wordz[i] == wordz[lenght-1]):
        flag = True
        lenght = lenght - 1
    else:
        flag = False
        break
if(flag):
    print("The word ",wordz," is a palindrome")
else:
    print("The word ",wordz," is not a palindrome")