'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Check if Employee is present or absent
        USing Switcher 
'''

import random


def emp_hrs_check(empcheck):
    '''
        Description: 
            emp_hrs_checks function is defined to check if the employee is present full time part time or absent.
        Function Parameters:
                a (random value generated)
        Return :
                emp_hrs
    '''
    switcher = {1: 8, 2: 4, 0: 0}
    return switcher[empcheck]


IS_PRESENT_FULL_TIME = 1
IS_PRESENT_PART_TIME = 2
EMP_RATE_PER_HR = 20

if __name__ == '__main__':
    emp_check = random.randint(0, 2)
    emp_hrs = emp_hrs_check(emp_check)
    salary = emp_hrs * EMP_RATE_PER_HR
    print(f"salary: {salary}")
