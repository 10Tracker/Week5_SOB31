# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) # int function missing

exam_three = int(input("Input exam grade three: ")) # not exam_3 because different value is used in list grade, also str is incorrect

grades = [exam_one, exam_two, exam_three] # added , for separating values
sum = 0
for grade in grades: # correction instead of 'for grade in grade' we are calling from variable grades for grade values.
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: # missing :
    letter_grade = "B"
elif avg >= 70 and avg < 80: # missing = after 70 ,incorrect range
    letter_grade = "C" # ' is used instead of " 
elif avg >= 60 and avg <70 : # < instead of >, incorrect range
    letter_grade = "D"
else:                   # correction else should be used in the end of if-elif statement, the for loop in the next line after letter_grade is removed since it is unncessary
    letter_grade = "F"     
    
print(f"Exam marks = {sum}") # using Formatted string to extract the right variables in the print statement
print(f"Average = {avg:.2f}")  # Limits to 2 decimal places
print(f"Grade: {letter_grade}")

if letter_grade == "F": # the symbol between letter grade is - instead underscore
    print ("Student is failing.") # missing brackets after print function
else:
    print ("Student is passing.") 

