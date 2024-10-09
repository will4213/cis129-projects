# Module 5 Lab
# Will McElwee
# 10-9-24
# The program lets you keep trak of the total number of bottles collected in a week

# Lab 5 The Bottle Return Program

# Declaring variables 
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'


# Loop to run program again
while keepGoing == 'y':
    while counter <= 7:
        # Code to set value of variables
        todayBottles = int(input('Enter number of bottles for day #' + str(counter) + ': '))
        
        # Code to set value of variable totalBottles
        totalBottles += todayBottles
        
        # Code to set value of variable totalPayout
        totalPayout = totalBottles * 0.10
        counter += 1
        
    # Code to print the number of total bottles and total payout
    print('Total amount of bottles collected is ' + str(totalBottles))
    print('The total paid out is $ ' + format(totalPayout, '.1f'))
    counter = 1
    totalBottles = 0
    totalPayout = 0
    print('Do you want to enter another week’s worth of data?')
    print('(Enter y or n)')
    keepGoing = input()	

