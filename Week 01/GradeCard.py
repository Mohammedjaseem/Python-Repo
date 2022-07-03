

def avg_written_test(mark):
    avg_written_test_mark=(mark*70)/100
    print("Your average written test is: ",avg_written_test_mark)
    return avg_written_test_mark

def avg_lab_exam(mark):
    avg_lab_exam_mark=(mark*20)/100
    print("Your average lab exam is: ",avg_lab_exam_mark)
    return avg_lab_exam_mark

def avg_assignments(mark):
    avg_assignments_mark=(mark*10)/100
    print("Your average assignments is: ",avg_assignments_mark)
    return avg_assignments_mark
    
def display_grade(as_mark,wt_mark,le_mark):
    total_mark = as_mark + wt_mark + le_mark
    grade=float(total_mark)
    print("Your grade is: ",grade)

def mark_avg_calculator():
    writen_test = int(input("Enter the written test scores: "))
    lab_exam = int(input("Enter the lab exam scores: "))
    assignments_mark = int(input("Enter the assignments scores: "))
    display_grade(avg_assignments(assignments_mark),
                  avg_written_test(writen_test),
                  avg_lab_exam(lab_exam))

# Calling the function    
mark_avg_calculator()