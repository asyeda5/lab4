#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input_string):
    return input_string[:5]  # Return the first five characters

def last_seven(input_string):
    return input_string[-7:]  # Return the last seven characters

def middle_number(num):
    num_str = str(num)  # Convert the number to string
    return num_str[1:3]  # Return the second and third characters

def first_three_last_three(str1, str2):
    return str1[:3] + str2[-3:]  # Combine first three of str1 and last three of str2

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
