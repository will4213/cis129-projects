#Will McElwee
#12-7-24
#This program lets the user input grades and returns the total, average, and the number of grades

#Puts the entered grades into a txt file, one grade per line
def writeGrades(grades):
    with open('grades.txt', 'w') as file:
        for grade in grades:
            file.write(f"{grade}\n")

#Gets the grades from the user and stops when they input 'done'
def getInput():
    while True:
        userInput = input("Enter a grade (or 'done' to finish): ")
        if userInput.lower() == 'done':
            break
        try:
            yield float(userInput)
        except ValueError:
            print('Invalid input, please enter a number')

#Returns the grades
def readGrades():
    grades = []
    try:
        with open('grades.txt', 'r') as file:
            for line in file:
                try:
                    grades.append(float(line.strip()))
                except ValueError:
                    print(f"Skipping invalid grade entry: {line.strip()}")
    except FileNotFoundError:
        print("No grades file found. Please add grades first.")
        return []
    return grades

#Displays the grades from the txt file and calculates the average and total
def displayGrades():
    grades = readGrades()
    if not grades:
        return

    print("Grades:")
    for grade in grades:
        print(grade)

    total = sum(grades)
    count = len(grades)
    average = total / count if count != 0 else 0

    print(f"\nTotal of grades: {total}")
    print(f"Number of grades: {count}")
    print(f"Average grade: {average:.2f}")

print("Enter grades. Type 'done' when finished:")
grades = list(getInput())
writeGrades(grades)
print(f"Grades have been saved to 'grades.txt'")
print("\nReading and displaying grades:")
displayGrades()
