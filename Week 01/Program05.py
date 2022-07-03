# Write a program to show the grade obtained by a student after he/she enters their total mark percentage.
# Program should accept an input from the user and display their grade

Total_mark = float(input("Enter the Total Mark: "))
if Total_mark >= 90:
    print("Grade A")
elif Total_mark >= 80:
    print("Grade B")
elif Total_mark >= 70:
    print("Grade C")
elif Total_mark >= 60:
    print("Grade D")
elif Total_mark >= 50:
    print("Grade E")
else:
    print("Failed")
