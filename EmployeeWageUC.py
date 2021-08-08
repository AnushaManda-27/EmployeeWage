'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Calculation wages for a month
        
'''
import random

IS_PRESENT_FULL = 1
IS_PRESENT_HALF = 2
EMP_RATE_PER_HR = 20
MAX_NO_OF_WORKINHG_DAYS = 20
totalWorkingDays = 0
totalEmpHrs = 0


def emp_hrs_check(empcheck):
    '''
        Description: 
            emp_hrs_checks function is defined to check if the employee is present full time part time or absent.
        Function Parameters:
                a (random value generated)
        Return :
                emp_hrs
    '''
    switcher = {1: 8, 2: 4, 0: 0}  # Here values are Working Hours
    return switcher[empcheck]

if __name__ == '__main__':

    while (totalWorkingDays < MAX_NO_OF_WORKINHG_DAYS):
        totalWorkingDays += 1
        emp_check = random.randint(0, 2)
        emphrs = emp_hrs_check(emp_check)
        #print(f"emphrs: {emphrs}")
        totalEmpHrs = totalEmpHrs + emphrs
        #print(totalEmpHrs)
    totalsalary = totalEmpHrs * EMP_RATE_PER_HR
    print(f"salary: Rs {totalsalary} ")
