# # #Q1)Add Two Numbers: Write a program that takes two numbers as input and prints their sum
# # a = int(input("Enter the 1st number: "))
# # b = int(input("Enter the 2nd number: "))
# # c = a + b
# # print(c)

# #Q2)Even or Odd: Create a program that checks if a given number is even or odd.
# l = 99
# if l%2 == 0:
#     print("It is a even number")
# else:
#     print("It is a odd number")

#Q3)Calculator: Write a simple calculator program that can perform addition, subtraction, multiplication, and division based on user input.
# x = int(input('Enter 1st number: '))
# y = int(input('Enter 2nd number: '))
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)

#Q4)Factorial Calculation: Write a program that calculates the factorial of a given number.
# num = int(input("enter a number: "))

# fact = 1

# if num<0:
#     print("Factorial of 0 doesnot exist")
# elif num ==0:
#    print("Factorial of 0 is",1)
# elif num>0:
#     for i in range (1,num+1):
#         fact = fact*i
# print("The factorial of the given number is",fact)

#Q5) Reverse a String: Create a program that takes a string as input and prints it in reverse order.
# def reverse_string(input_string):
#     reverse_string = input_string[::-1]
#     return reverse_string

# #input from user
# input_string = input("Enter a string: ")

# #calling the function
# reversed_result = reverse_string(input_string)

# #print the reversed string
# print("Reversed string:",reverse_string(input_string))

#Q6)List Manipulation: Given a list of numbers, write a program to find the sum, average, maximum, and minimum values in the list.


#Q7)Palindrome Checker:Write a program that checks if a given string is a palindrome(reads the same forwards and backwards)
# a = input("enter a word here: ")

# l = a[::-1]

# if a == l:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

#Q8)Leap Year Checker: Create a program that checks if a given year is a leap year or not.
# year = int(input("enter a year: "))

# if (year %400 == 0 ) and (year %100 == 0):
#    print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")

#Q9) Fibonacci Sequence: Write a program to generate the first N terms of the Fibonacci sequence.

#Q10)Prime Number Checker: Write a program to check if a given number is a prime number.

# num = int(input("Enter a number: "))
# if num == 1:
#     print("it is not a prime number")

#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 print('not prime')
# else:
#     print("it is a prime number")

#Q11)Simple To-Do List: Create a simple to-do list program that allows users to add, remove, and view tasks.

#Q12)Guess the Number Game: Implement a number guessing game where the computer picks a random number, and the player has to guess it.

# import random

# num = int(input("Type a number: "))

# if num.isdigit():
#     num = int(num)

#     if num<= 0 :
#         print()