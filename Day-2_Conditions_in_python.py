#Strings 

str1 = "This is a string"
str2 = 'This is also a string'
str3 = """This is also a string"""


str4 = "This is a string *using \n*escape characters \ n for new line and \t for tab space \ t"
print(str4)

#Concatenation of strings

Final_string = str1 + " " + str2 + " " + str3
print(Final_string)

# To find the length of a string we use the len() function
print(len(Final_string))

##String indexing
#Strings are indexed in python, we can access the characters of a string using their index number
string = "Gyanendra"
print(string[0]) #G
print(string[1]) #y
print(string[2]) #a
print(string[3]) #n
print(string[4]) #e
print(string[5]) #n
print(string[6]) #d
print(string[7]) #r
print(string[8]) #a

#string[0] = "A" #Error: 'str' object does not support item assignment
# Slicing of strings
#we can slice a string using the slicing operator [:]
print(string[0:5]) #Gyan    
print(string[5:8]) #endra
print(string[0:]) #Gyanendra
print(string[0:5:2]) #Gae
print(string[0::-1])#G
print(string[0:len(string)])

# - indexing
print(string[-1]) #a
print(string[-2]) #r
print(string[-3]) #d
print(string[-4]) #n
print(string[-5]) #e
print(string[-6]) #n
print(string[-7]) #a
print(string[-8]) #y
print(string[-9]) #G

## String Functions
# 1. upper() - converts all characters in a string to uppercase
string = "hello world"
print(string.upper())

# 2. lower() - converts all characters in a string to lowercase
print(string.lower())

# 3. capitalize() - converts the first character of a string to uppercase
print(string.capitalize())

# 4. title() - converts the first character of each word in a string to uppercase
print(string.title())

# 5. swapcase() - swaps the case of all characters in a string
print(string.swapcase())

# 6. count() - counts the number of occurrences of a substring in a string
print(string.count("o"))

# 7. find() - returns the index of the first occurrence of a substring in a string
print(string.find("o"))

# 8. replace() - replaces all occurrences of a substring in a string with another substring
print(string.replace("world", "Python"))

# 9. strip() - removes leading and trailing whitespace from a string
string_with_whitespace = "   hello world   "
print(string_with_whitespace.strip())

# 10. split() - splits a string into a list of substrings based on a delimiter
print(string.split(" "))

#11. endswith() - returns True if a string ends with a specified suffix, otherwise False
print(string.endswith("world"))

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