###################################################
#Josue Cifuentes
#CIS 225
#1) Number of errors found: 13
#2) Error Types: NameError on line 44 missing int(
#                NameError on line 46 should be int instead of str
#                NameError on line 46 should be exam_three
#                NameError on line 48 should be grade not grades
#                NameError on line 50 should be len(grade)
#                SyntaxError on line 48 missing commas separating exam numbers
#                SyntaxError on line 59 should be " instead of '
#                SyntaxError on line 55 missing a :
#                SyntaxError on line 65 missing avg < 65:
#                SyntaxError on line 74 missing () after print
#                SyntaxError on line 76 missing () after print
#                NameError on line 73 should say letter_grade
#                NameError line 66 should say for grade in letter_grade
####################################################
# Program Name: grading.py
# Purpose of a program:
# Write a program computing an average of three exam scores
# User enters three exam scores.
# Program prints the exam scores, average of three scores, corresponding letter grade,
# and result of Pass or Fail of a course.


# To pass a course, student should get a grade C or above.

# Average Score    Grade
#    90+	        A
#    80-89	        B
#    70-79	        C
#    60-69	        D
#    0-59	        F

# Example of output
# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

#place a comma to separate each exam score
#grade = [exam_one, exam_two, exam_three]
grade = [exam_one + exam_two + exam_three]
sum = 0

#grade is a loop variable and grades is a list holding exam scores.
#for grade in grades:
#    sum = sum + grade
for grade in grade:
  sum = sum + grade

#Use len function to get total number of elements in the list grades
#avg = sum/len(grades)
avg = sum / 3

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:   #elif avg >= 70 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65: #elif avg >= 60 and avg < 70:
    letter_grade = "D"
elif avg < 65:                #else:
    letter_grade = "F"
for grade in letter_grade:
    print("Exam: " + str(grade))

#No indentation necessary because average and grade should be printed once.
#Also you can use a format function.
#print("Average: {}".format(avg))
#print("Grade: {}".format(letter_grade))
    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
