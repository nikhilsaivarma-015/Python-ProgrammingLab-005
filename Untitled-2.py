# Student Academic Performance Analyzer
# Reads student details and marks, then computes total, average, percentage and grade
 
# Read student name and USN
student_name = input("Enter Student Name: ")
student_usn = input("Enter USN: ")
 
# Accept marks in five subjects (type conversion: str -> float)
mark1 = float(input("Enter Marks in Subject 1 (out of 100): "))
mark2 = float(input("Enter Marks in Subject 2 (out of 100): "))
mark3 = float(input("Enter Marks in Subject 3 (out of 100): "))
mark4 = float(input("Enter Marks in Subject 4 (out of 100): "))
mark5 = float(input("Enter Marks in Subject 5 (out of 100): "))
 
# Calculate total, average and percentage
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
average_marks = total_marks / 5
percentage = total_marks / 5   # each subject is out of 100, so total/5 gives percentage
 
# Assign grade based on percentage
if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "RA"
 
# Display the report using f-strings
print("\n------- STUDENT PERFORMANCE REPORT -------")
print(f"Student Name : {student_name}")
print(f"USN          : {student_usn}")
print(f"Total Marks  : {total_marks:.2f}")
print(f"Average      : {average_marks:.2f}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
