# elif statement
"""
-> Syntax:
            if <cond1>:
                TSB1
            elif <cond2>:
                TSB2
            .
            .
            .
            elif <condn>:
                TSBn
            else:
                FSB
"""

# 1) WAP to compare 2 numbers
# num1 = int(input('Enter the first number : '))
# num2 = int(input('Enter the second number : '))
# if num1 > num2:
#     print('num1 is greater')
# elif num1 < num2:
#     print('num2 is greater')
# else:
#     print('num1 and num2 are equal')

# 2) WAP to check the type of character
# ch = '$'
# if 'A' <= ch <= 'Z':
#     print('Uppercase')
# elif 'a' <= ch <= 'z':
#     print('Lowercase')
# elif '0' <= ch <= '9':
#     print('Number')
# else:
#     print('Special Character')

"""
3) WAP to consider integer input, print FIZZ if the number is divisible by 5, print BUZZ if 
   the number is divisible by 7, print FIZZ BUZZ if the number is divisible by both 5 and 7.
   print Hello World if the number is neither divisible by 5 nor 7
"""

# num = 150
# if num % 5 == 0 and num % 7 == 0:
#     print('FIZZ BUZZ')
# elif num % 7 == 0:
#     print('BUZZ')
# elif num % 5 == 0:
#     print('FIZZ')
# else:
#     print('HELLO WORLD')

"""
4) WAP to consider integer input and print the number of digits of the number. 
   Your answer should be single digit, two digit, three digit or more than 3 digit
"""

# num = int(input())
# if 0 <= num <= 9:
#     print('Single Digit')
# elif 10 <= num <= 99:
#     print('Double Digit')
# elif 100 <= num <= 999:
#     print('Three Digit')
# elif num > 999:
#     print('More than 3 digit')
# else:
#     print('Invalid Input')

"""
5) WAP to consider marks of a student as input and print  the grade based on the marks 
   obtained. 
"""

# marks = int(input('Enter the marks out of 100 : '))
# if 90 <= marks <= 100:
#     print('A')
# elif 75 <= marks < 90:
#     print('B')
# elif 55 <= marks < 75:
#     print('C')
# elif 40 <= marks < 55:
#     print('D')
# elif 35 <= marks < 40:
#     print('E')
# elif 0 <= marks < 35:
#     print('F')
# else:
#     print('Invalid marks')

# 6) WAP to print the highest among 3 distinct numbers

num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 > num2 and num1 > num3:
    print('num1 is greater')
elif num2 > num3:
    print('num2 is greater')
else:
    print('num3 is greater')

# 7) WAP to print the lowest among 4 distinct numbers














