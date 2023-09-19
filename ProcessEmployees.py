'''
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
'''

import csv

#open the file

Employee_Data = open("employee_data.csv","r")

EmployeeData_Infile = csv.reader(Employee_Data, delimiter=",")

skip = next(EmployeeData_Infile)


#create an empty dictionary

EmployeeNew_Salary = {}

#use a loop to iterate through the csv file

total_current = 0.0
total_new = 0.0
for r in EmployeeData_Infile:
    #check if the employee fits the search criteria

    if r[9] == 'TS' and r[3] == 'Marketing' and r[4]=='CSR':
        
        emp_name = r[1]+' '+r[2]
        current_salary = int(r[5])
        total_current += current_salary
        print(f'Employee Name: {emp_name} Current Salary: ${current_salary:.2f}')

        up_salary = current_salary + (current_salary*.10)

        EmployeeNew_Salary[emp_name] = up_salary
        total_new += up_salary
    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per image

for rep in EmployeeNew_Salary:
    print(f'Employee Name: {rep} New Salary: ${EmployeeNew_Salary[rep]:.2f}')
         

print()
print('=========================================')
print()

#print out the total difference between the old salary and the new salary as per image.
total_increase = total_new - total_current
print(f'Total Increase in Salary:${total_increase:.2f}')
