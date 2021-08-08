

'''
@Author: Anusha Manda
@Date: 2021-08-05 12: 00: 30
@Last Modified by: Anusha Manda
@Last Modified time: 2021-08-06 18: 00: 30
@Title: Check if Employee is present or absent
'''
import random

if __name__ == '__main__':
    print("welcome to Employee wage ")

    IS_PRESENT = 1
    emp_check = random.randint(0, 1)
    if (emp_check == IS_PRESENT):
        print("Employee is Present")
    else:
        print("Employee is absent")
