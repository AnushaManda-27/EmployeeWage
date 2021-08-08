'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Check if Employee is present or absent
        Employee hours for full time is 8
        Employee hours for part time is 4
'''

import random

IS_PRESENT_FULL_TIME = 1
IS_PRESENT_PART_TIME = 2
EMP_RATE_PER_HR = 20

if __name__=='__main__':
    emp_check = random.randint(0, 2)
    if(emp_check == IS_PRESENT_FULL_TIME):
        emp_hrs = 8
        print("employee present full time")
    elif(emp_check == IS_PRESENT_PART_TIME):
        emp_hrs = 4
        print("Employee is present half time")
    else:
        emp_hrs = 0
        print("Employee is absent")

salary = emp_hrs * EMP_RATE_PER_HR
print("salary: "+str(salary))
