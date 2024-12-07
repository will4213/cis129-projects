#Will McElwee
#12-7-24
#This program lets a user input the name of a student and their grades for three exams
#and saves it to a csv file

import csv

# Open the file in write mode
with open('grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    #Function to get student data
    def getStudentInfo():
        firstName = input("Enter student's first name: ").strip()
        lastName = input("Enter student's last name: ").strip()

        #Input for each exam grade
        exam1 = int(input("Enter grade for Exam 1: "))
        exam2 = int(input("Enter grade for Exam 2: "))
        exam3 = int(input("Enter grade for Exam 3: "))

        return [firstName, lastName, exam1, exam2, exam3]

    #Loop to enter multiple students' data
    while True:
        studentData = getStudentInfo()
        writer.writerow(studentData)

        #Ask if there is another student to add
        another = input("add another student? (y/n): ").lower()
        if another != 'y':
            break

print("Grades have been saved to grades.csv")
