# # #Strings 

# str1 = "This is a string"
# str2 = 'This is also a string'
# str3 = """This is also a string"""


# # str4 = "This is a string *using \n*escape characters \ n for new line and \t for tab space \ t"
# print(str4)

# # #Concatenation of strings

# # Final_string = str1 + " " + str2 + " " + str3

# print(Final_string)

# # # To find the length of a string we use the len() function

# print(len(Final_string))

# # ##String indexing
# # #Strings are indexed in python, we can access the characters of a string using their index number

# string = "Gyanendra"
# print(string[0]) #G
# print(string[1]) #y
# print(string[2]) #a
# print(string[3]) #n
# print(string[4]) #e
# print(string[5]) #n
# print(string[6]) #d
# print(string[7]) #r
# print(string[8]) #a

# # #string[0] = "A" #Error: 'str' object does not support item assignment
# # # Slicing of strings
# # #we can slice a string using the slicing operator [:]

# print(string[0:5]) #Gyan    
# print(string[5:8]) #endra
# print(string[0:]) #Gyanendra
# print(string[0:5:2]) #Gae
# print(string[0::-1])#G
# print(string[0:len(string)])

# # # - indexing

# print(string[-1]) #a
# print(string[-2]) #r
# print(string[-3]) #d
# print(string[-4]) #n
# print(string[-5]) #e
# print(string[-6]) #n
# print(string[-7]) #a
# print(string[-8]) #y
# print(string[-9]) #G

# ## String Functions
# # 1. upper() - converts all characters in a string to uppercase


# string = "hello world"
# print(string.upper())

# # 2. lower() - converts all characters in a string to lowercase

# print(string.lower())

# # 3. capitalize() - converts the first character of a string to uppercase

# print(string.capitalize())

# # 4. title() - converts the first character of each word in a string to uppercase

# print(string.title())

# # 5. swapcase() - swaps the case of all characters in a string

# print(string.swapcase())

# # 6. count() - counts the number of occurrences of a substring in a string

# print(string.count("o"))

# # 7. find() - returns the index of the first occurrence of a substring in a string

# print(string.find("o"))

# # 8. replace() - replaces all occurrences of a substring in a string with another substring

# print(string.replace("world", "Python"))

# # 9. strip() - removes leading and trailing whitespace from a string

# string_with_whitespace = "   hello world   "
# print(string_with_whitespace.strip())

# # 10. split() - splits a string into a list of substrings based on a delimiter

# print(string.split(" "))

# #11. endswith() - returns True if a string ends with a specified suffix, otherwise False

# print(string.endswith("world"))

# 1 Practice Question -> Take the input of a user's name and print its length

name = input("Enter you name : ")
print("Your name length is : ",len(name)) 

# 2 Practice Question -> Write a program to find occurrence of 'S' in a string

string1 = input("Enter a string : ")
print("Occurrence of 'S' in the string is : ",string1.count("S"))

#Conditional Statments in Python
# if, elif, else

light = "yellow"

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get Ready")
else:
    print("Go")

# Taking input from user form user and give them grade accourding to there number 

Marks = int(input("Enter your marks : "))
if Marks >= 90:
    print("Your grade is A")
elif ( Marks >= 80 and Marks < 90):
    print("Your grade is B")
elif (Marks >= 70 and Marks < 80):
    print("Your grade is C")
elif (Marks >= 60 and Marks < 70):
    print("Your grade is D")
else:
    print("Your grade is F")

## Practice Questions 1 
## Write a program to check if a number entered by the user is odd ar even

number =int(input("Enter your number to check is it odd or even : "))
if number % 2 == 0:
    print("The number you are entered " +str(number) +" is even")
else:
    print("The number you enterd is  " +str(number) +" is odd")
 
# Practice questions 2
# Write a program to find gratest of 3 numbers eneterd by user 

Number_1 = int(input("Enter your first number : "))
Number_2 = int(input("Enter your second number : "))
Number_3 = int(input("Enter your thired number : "))

print("The gratest number is : ",max(Number_1,Number_2,Number_3))
print(" OR by if else statement")
if Number_1 > Number_2 and Number_1 > Number_3:
    print("The gratest number is : ",Number_1)
elif Number_2 > Number_1 and Number_2 > Number_3:
    print("The gratest number is : ",Number_2)
else:
    print("The gratest number is : ",Number_3)  

# Practice questions 3
# Write a program to check if a number is Multiple od 7 or not.

number = int(input("Enter a number : "))
if number % 7 == 0:
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")
    
###############################################################################

# Mini - Project 
name = input("Enter your name : ")
marks_python = int(input("Enter your marks in python : "))
marks_sql = int(input("Enter your marks in sql : "))
marks_maths = int(input("Enter your marks in maths : "))
average_marks = (marks_python + marks_sql + marks_maths) / 3
if average_marks >= 90:
    grade = "A"
elif average_marks >= 75 and average_marks <=89:
    grade = "B"
elif average_marks >= 60 and average_marks <=74:
    grade = "C"
elif average_marks >= 40 and average_marks <=59:
    grade = "D"
else:
    grade = "F"

result = "Pass" if average_marks >= 40 else "Fail"

attendance = int(input("Enter your attendance percentage : "))

print("Name : ", name)
print("Average Marks : ", average_marks)
print("Grade : ", grade)
print("Result : ", result)
if attendance >= 75 and result == "Pass":
    print("Attendance : ", attendance, "% (Eligible for exam: Yes)")
else:
    print("Attendance : ", attendance, "% (Eligible for exam: No)")

#
# Problem 1 -> take a number and determine whether it is positive even, positive odd , negative odd , negative even or zero
number = int(input("Enter a number : "))
if number > 0:
    if number % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
elif number < 0:
    if number % 2 == 0:
        print("The number is negative and even")
    else:
        print("The number is negative and odd")
else:
    print("The number is zero")

## Problem 2 -> Take a number age determine that he is chile , teeager , adult or senior
age  = int(input("Enter your age : "))

if age > 0 and age <=12 :
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a Teenager")
elif age >= 20 and age <= 59:
    print("You are a Adult")
else:
    print("You are a Senior")

## Problem 3 -> Create a simple login system
username = input("Enter your user name : ")
password = input("Enter your password : ")
if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Login failed")

## Problem 4 -> Take electricity units and calculate the bill using different uasge ranges
units = int(input("Enter the number of unites consumed : "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
print("The electricity bill is : ", bill)

## Problem 5 -> Take 3 numbers and find the largest number without using max()
number = int(input("Enter first number : "))
number1 = int(input("Enter second number : "))
number2 = int(input("Enter third number : "))
if number > number1 and number > number2:
    print("The largest number is : ", number)
elif(number1 > number and number1 > number2 ):
    print("The largest number is : ", number1)
else:
    print("The largest number is : ", number2)
