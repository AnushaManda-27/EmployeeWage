'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Check if Employee is present or absent
        employee work hours is 8
        employee rate per hour is 20
'''


import random

if __name__=='__main__':
    IS_PRESENT = 1
    EMP_RATE_PER_HR = 20
    emp_check = random.randint(0, 1)
    if (emp_check == IS_PRESENT):
        emp_hrs = 8
    else:
        emp_hrs = 0
    salary = (EMP_RATE_PER_HR * emp_hrs)
    print(f"salary:{salary}")
