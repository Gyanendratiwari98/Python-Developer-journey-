## LOOP ## 
# Python loop for , while , range() , break , continue , pass , nested loop , else in loop , infinite loop , for else , while else , loop control statements
# why loop ??
print("Python")
print("Python")
print("Python")
print("Python")
print("Python")

# with loop 

############## FOR LOOP ##############

print("With loop")
for i in range(50):
    print("Python")

for i in range(2, 100,2):
    print(i)

#       range(stop)
#    range(start, stop)
#   range(start, stop, step)
for i in range(10, 0, -1):
    print(i)

# Loop though Strings
name = "Gyanendra"
for i in name:
    print(i)

languages = ["Python", "Java", "C++", "C#", "JavaScript"]
for i in languages:
    print(i)

## While Loop ##

number = 0
while number < 10:
    print(number)
    number +=1

number = 0 
while number < 10:  # infinite loop
    print(number)

for i in range(1,11):
    if i == 7:
        break # Break the loop when i is equal to 7
    print(i)

for i in range(1,11):
    if i == 7:
        continue  # Skip the rest of the code in the loop for this iteration and move to the next iteration
    print(i)

##break -> Stop the loop

# continue -> Skip one iteration
## 1 to 10 table using nested loop
for i in range(1, 11):
    for j in range(1,11):
        print(i, "*", j, "=", i*j)

# print 1 to 100 
for i in range(1, 101):
    print(i, end=" ")

## even number 1 to 100
for i in range(2,101,2):
    print(i, end=" ")

## odd number 1 to 100
for i in range(1,101,2):
    print(i, end=" ")

## print sum of 1 to 100 using while loop
i = 1 
sum = 0
while i <= 100:
    sum+=i
    i+=1
print("Sum of 1 to 100 is :", sum)

## Plain text ###
number = int(input("Enter a number : "))
for i in range(11):
    print( i  , " X " ,  number , " = " ,i*number  )   

# Countdown 10 to GO!

for i in range(10, 0, -1):
    print(i)
print("GO!")

# Python Developer count character
str = "Python Developer"
count = 0
for i in str:
    count+=1
print(count)

## Vowel Counter 
sentence = "Gyanendra Tiwari"
sentence =sentence.lower()
vowels = ["a","e","i","o","u"]
count = sum(1 for char in sentence if char in vowels)
print("Number of vowels : " , count)

## Break 
## Without break
num = int(input("Enter a number : "))
while num != 0 :
    num = int(input("Enter a number : "))
print(" !!! Program stopped !!! ")

## With Break
while 1 > 0 :
    num = int(input("Enter the number : "))
    if num == 0 :
        break
print("!!! Program stopped !!!")

##Continue 
## Problem -> Print numbers from 1-30 but skip numbers divisible by 3.
for i in range(31):
    if i % 3 == 0:
     continue
    else :
     print("Number is :  ", i)
############### MINI Project #############
print("How many numbers do you want to enter ? ")
num = int(input())
positive_number = 0
negative_number = 0
even = 0 
odd = 0
total = 0
zero = 0
if num <= 0 :
   print("Please enter at least one number.")
else :
    for i in range(num):
     user_num = int(input("Enter number " + str(i+1) + " : "))
     if user_num > 0 :
        positive_number += 1 
     elif user_num == 0 :
        zero += 1
     else:
        negative_number += 1

     if user_num % 2 == 0 :
        even +=1
     else:
        odd += 1
     total +=user_num
average = total/num
print("------------ ANALYSIS ---------------")

print("Total number : ", num)
print("Positive numbers : " , positive_number)
print("Negative numbers : " , negative_number)
print("Zero : ",zero)

print("Even numbers : ", even)
print("Odd numbers  : ", odd)

print("Sum : ",sum)
print("Average : ",average)


    
        
    
    



