
# # Starting python revision 
# # Print -> funtion is used to print the output on the console
# print("Hello world")
# print("Hi....... my name is gyanendra tiwari and this my python learning journey ")
# print("Starting my python revision from 0 and aming to go 100 % this time .")

# # Variables -> Variables are used to store the data in python
# # Variable name should be meaningful and should not start with number or special character
# name ="gyanendra tiwari"
# age = 22
# price = 11.11

# print("My name is :" , name)
# print("My age is :" , age)
# print("My price is :" , price)
# print("My name is :" + name , "My age is :" + str(age) , "My price is :" + str(price))
# print("My name is :" , name , ", My age is :" , age , ", My price is :" , price)

# #Data types -> Data types are used to define the type of data we are storing in the variable
# # There are 5 main data types in python -> int , float , str , bool , None .

# name = "gyanendra tiwari" # str
# age = 22 # int
# price = 11.11 # float
# is_student = True # bool
# height = None # None


# print("My name is :" , name , "and its data type is :" , type(name))
# print("My age is :" , age , "and its data type is :" , type(age))
# print("My price is :" , price , "and its data type is :" , type(price))
# print("Is student :" , is_student , "and its data type is :" , type(is_student))    
# print("My height is :" , height , "and its data type is :" , type(height))


# # type of operators 
# # Airthamatic operators -> + , - , * , / , % , **
# a = 100
# b = 20
# sum = a + b
# print("The sum of a and b is :" , sum)

# diff = a - b
# print("The difference of a and b is :" , diff)

# product = a * b
# print("The product of a and b is :" , product)

# quotient = a / b
# print("The quotient of a and b is :" , quotient)

# mod = a % b
# print("The remainder of a and b is :" , mod)

# print("a to the power of b is :" , a ** b) #a^b


# # Relational/comparision operators -> == , != , > , < , >= , <=
# x = 10 
# y = 60
# print("x == y :" , x == y)
# print("x != y :" , x != y)
# print("x > y :" , x > y)
# print("x < y :" , x < y)
# print("x >= y :" , x >= y)
# print("x <= y :" , x <= y) 


# # assigment operators -> = , += , -= , *= , /= , %= , **=
# x = 10
# x += 5  # x = x + 5
# print("x ofter x += 5 is :" , x)
# x -= 5 # x= x-5
# print ( "x ofter x -= 5 is :" , x)
# x *= 5 # x = x * 5
# print("x ofter x *=5 is :" ,x)
# x/=5 # x =x/5
# print("x ofter x /=5 is :" ,x)
# x%=5 # x = x%5
# print("x ofter x %=5 is :" ,x)
# x**=5 # x = x**5
# print("x ofter x **=5 is :" ,x)


# # Logical operators -> and , or , not
# a = True
# b = False
# print("a and b :" , a and b)
# print("a or b :" , a or b)
# print("not a :" , not a) 

#  # Type conversion -> Type conversion is used to convert one data type to another data type

# a = 2 #int 
# b = 3.5 #float 
# sum = a + b #int + float = float
# print(sum)
# print(type(sum)) # a is automaticlly converted to float , This is called type conversion

# # Type casting -> type casting is used to convert one data type to another data type explicitly
# a = 2 #int
# print(type(a))
# a = int(a)
# #print(type(a))

# #Input in python -> input() function is used to take input from the user

# # Name = input("Enter your name : ")
# # Age = int(input("Enter your Age : "))
# # salary = float(input("Enter your Salary : "))
# # print("Welcome " + Name + " your age is only " + str(Age) + " you will get a job with salary " + str(salary) + " Soon (in one month). ")

# #Practice ->
# # #1
# # a = int(input("Enter frist number : "))
# # b = int(input("Enter number 2nd  :"))
# # Sum = a + b
# # print("The sum of " + str(a) + " and " + str(b) + " is :" + str(Sum))

# # #2
# # side = float(input("Enter the side of Squre : "))
# # area = side * side
# # print("Area of a square is :" + str(area))

# # #3
# # a = int(input("Enter the number : "))
# # b = int(input("Enter the number : "))
# # print(a>=b)

# # #4
# # name = input("Enter your name : ")
# # age = int(input("Enter your age : "))
# # salary = float(input("Enter your salary : "))
# # expense = float(input("Enter your monthly expense : "))
# # print("Your annual salary is :" + str(salary*12))
# # print("Your annual Savings is :" + str((salary*12) - (expense*12)))

# # #5
# # a = int(input("Enter first number : "))
# # b = int(input("Enter second number : "))
# # print("The sum of " + str(a) + " and " + str(b) + " is :" + str(a+b))
# # print("The Product of " + str(a) + " and " + str(b) + " is :" + str(a*b))
# # print("The difference of " + str(a) + " and " + str(b) + " is :" + str(a-b))
# # print("The division of " + str(a) + " and " + str(b) + " is :" + str(a/b))

# # #6
# # age = int(input("Enter your age : "))
# # print("Your age after ten years from now will be :" + str(age+10))

# # #7
# # temprature = float(input("Enter the temperature in celsius : "))
# # print("The tempature in fahrenheit is :" + str((temprature * 9/5) +32))

# # #8
# # lenght = float(input("Enter the lenght of rectangle : "))
# # breath = float(input("Enter the breath of rectangle : "))
# # area = lenght * breath
# # print("The area of rectangle is :" + str(area))

# # #9
# # Monthly_salary = float(input("Enter your monthly salary : "))
# # Annual_salary = (Monthly_salary + Monthly_salary/10)* 12
# # print("Your annual salary after increment of 10% is :" + str(Annual_salary))
