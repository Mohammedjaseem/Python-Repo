# Write a program to check whether a student has passed or failed in a subject after he or she enters their mark (pass mark for a subject is 50 out of 100).
# Program should accept an input from the user and output a message as “Passed” or “Failed”


Mark = float(input("Enter the Mark: "))
if Mark >= 50:
    print("Exam Passed")
else:
    print("Exam Failed")