'''
Grades are computed using a weighted average. Suppose that the written test counts 70%,  lab exams 20% and assignments 10%.
If Arun has a score of
Written test = 81
Lab exams = 68
Assignments = 92
Arun’s overall grade = (81x70)/100 + (68x20)/100 + (92x10)/100 = 79.5
 Write a program to find the grade of a student during his academic year. 
Program should accept the scores for written test, lab exams and assignments
Output the grade of a student (using weighted average)
Eg:
Enter the marks scored by the students
Written test = 55
Lab exams = 73
Assignments = 87
Grade of the student is 61.8


'''

def avg_written_test(mark):
    avg_written_test_mark=(mark*70)/100
    print("\n Average Written test is: ",avg_written_test_mark)
    return avg_written_test_mark

def avg_lab_exam(mark):
    avg_lab_exam_mark=(mark*20)/100
    print("\n Average Lab exam is: ",avg_lab_exam_mark)
    return avg_lab_exam_mark

def avg_assignments(mark):
    avg_assignments_mark=(mark*10)/100
    print("\n Average Assignments is: ",avg_assignments_mark)
    return avg_assignments_mark
    
def display_grade(as_mark,wt_mark,le_mark):
    total_mark = as_mark + wt_mark + le_mark
    grade=float(total_mark)
    print("\n Your grade is: ",grade)

def mark_avg_calculator():
    writen_test = int(input("Enter the written test scores: "))
    lab_exam = int(input("Enter the lab exam scores: "))
    assignments_mark = int(input("Enter the assignments scores: "))

    #passing values to the functions
    display_grade(avg_assignments(assignments_mark),
                  avg_written_test(writen_test),
                  avg_lab_exam(lab_exam))

# Calling the function    
mark_avg_calculator()