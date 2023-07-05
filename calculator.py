'''
This script let the use choose from two choices:
1. a simple calculator 
2. read equation and calculate the result 

For choice 1:
User needs to enter two numbers and the operation (e.g. +, -, x, etc.).
The equation along with the result will be displayed
All equations will be save to a txt file

For choice 2:
User needs to input the file name.
The eaquations within the file will be read, calculated, and printed along with the results.
'''
import operator
import os

operator_dict={
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,  
    '/':operator.truediv  
}
# Choice 1 or choice 2
while True:
    option=input('Please enter "1" for calculator, and "2" for reading equations from a txt file: ')
    if not (option=='1' or option=='2'):
        print('Please enter a valid input.')
    else:
        break
# 1. a simple calculator     
if option=='1':
    equation=[]
    i=0

    while True:

        while True:
            try:
                number1=float(input('Please enter the first number:'))
                break
            except ValueError:
                print('Please enter a valid value.')

        while True:
            try:
                number2=float(input('Please enter the second number:'))
                break
            except ValueError:
                print('Please enter a valid number.')

        while True:
            operation=(input('Please choose operation (+, -, *, /):'))
            if not ((operation=='+') or (operation=='-')or (operation=='*')or (operation=='/')):
                print('Please enter a valid operation.')
            else:
                break

        try: 
            answer=operator_dict[operation](number1, number2)
            equation_loop=str(number1)+operation+str(number2)+'='+str(answer)
            equation=equation+[equation_loop]
            print(equation_loop)
        except ZeroDivisionError:
            print('Please do not divide over 0')
 
        # user choose if to input another equation
        while True:
            another_equation= input('Do you want to input another equation? (Y/N)')
            if not ((another_equation.upper()=='N')or(another_equation.upper()=='Y')):
                print('Please enter a valid answer.')
            else:
                break
        
        if (another_equation.upper()=='Y'):
            print('Please enter another equation:')
        else:
            break



    file_text='\n'.join(equation[0:])
    print('All the equations along with the results are:')
    print(file_text)
    text_file = open("equation_calculation.txt", "w")
    text_file.write(file_text)
    text_file.close()
    print('Saved to',os.getcwd())

# 2. read equation and calculate the result 
elif option=='2':
    while True:
        try:
            file_name=input('Please input the txt file name (eg. sample.txt):')

            with open(file_name) as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    print(line)
            break
        
        except FileNotFoundError:
            print('Please input a valid txt file name, and check if the file is stored in the path:',os.getcwd())     
            


