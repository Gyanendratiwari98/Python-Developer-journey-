# ## Python String ##
# name = "Gyanendra tiwari"
# city = 'jabalpur'

# message = """This is a multo-line string."""

# ## String indexing 

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7])
# print(name[8])

# ###    Reverse   ###

# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])
# print(name[-5])
# print(name[-6])
# print(name[-7])
# print(name[-8])
# print(name[-9])

# ### Slicing ###

# print(name[0:9])
# print(name[:3])
# print(name[2:])
# print(name[::2])
# print(name[::-1])

# ### Changes case ###

# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.capitalize())
# print(name.strip())
# print(name.replace("Gyanendra","GOT"))
# print(name.find("tiwari"))
# print(name.count("a"))
# print(name.startswith("Gyan"))
# print(name.endswith("ari"))
# print(name.split())


# words = ["Python", "is", "powerful"]

# sentence = " ".join(words)

# print(sentence)

# split() → string → list

# join() → list → string

# The f-string in Python is a concise and efficient way to format strings by embedding expressions directly within string literals. Introduced in Python 3.6, it simplifies string interpolation.

# name = "Gyanendra"
# age = 22

# print(f"My name is {name} and I am {age} years old.")

# ### Exercise 1 -> Character Access
# text = "PythonDeveloper"

# # First character
# # Last character
# # 5th character
# # First 6 characters
# # Last 5 characters

# print(text[0])
# print(text[-1])
# print(text[4])
# print(text[0:6])
# print(text[9:len(text)])


# ### Exercise 2 -> Reverse
# ## using Slicing

# text = "Python"

# print(text[::-1])

# ### Exercise 3 -> Case Converter

# plain_text = "python developer"

# print(plain_text.upper())
# print(plain_text.title())
# print(plain_text.lower())

# ### Exercise 4 -> Count a Character

# Sen = input("Enter a sentence : ")
# ch  = input("Enter a character : ")
# print(Sen.count(ch))

# ### Word Counter
# text = input("Enter the text : ")
# print("Number of words : ",len(text.split()))

# ### Email Validator 
# email = input("Enter your email id : ")
# if "@" in email and "." in email and not email.startswith("@"):
#     print(f"Email -> {email} is -> Valid")
# else :
#     print(f"Email -> {email} is -> Invalid")


# ########################## Mini Project #############################

# para = input("Enter a paragraph : \n")
# print("\n " , para)

# print("\n========== TEXT ANALYSIS ============\n")

# Characters = len(para)

# print("Characters : ", Characters)

# words = para.split()

# print("Words : ",len(words))

# lines = para.splitlines()

# print("Lines : " , len(lines))

# uppercase = 0 

# for i in para :
#     if i.isupper():
#      uppercase +=1
# print("Uppercase characters : " , uppercase)



# Lowercase = 0 

# for i in para :
#     if i.islower():
#      Lowercase +=1
# print("Lowercase characters : " , Lowercase)


# digits = 0

# for i in para:
#    if i.isdigit():
#       digits+=1
          
# print("Digits : ",digits)


# space = 0 
# for char in para:
#    if char  == " ":
#       space+=1
# print("Spaces : ",space)


# vowel_count = 0

# vowels = "aeiou"

# for char in para.lower():
#    if char in vowels:
#       vowel_count+=1
# print("Vowels : ",vowel_count)



# consonants = 0

# for char in para.lower():
#    if char.isalpha() and char not in vowels:
#       consonants += 1

# print("Consonants : ", consonants)



# words = para.lower().split()

# clean_words = []

# for word in words:
#    word = word.strip(".,!?")
#    clean_words.append(word)


# most_common_word = ""
# highest_count = 0

# for word in clean_words:

#    count = 0

#    for current_word in clean_words:

#       if word == current_word:
#          count += 1

#    if count > highest_count:
#       highest_count = count
#       most_common_word = word

# print(f"Most common word is  : {most_common_word} it come {highest_count} time in paragraph")

# ## Search for a word 

# search_word = input("Search word : ").lower()

# search_count = 0 

# for current_word in clean_words:
#    if current_word == search_word:
#       search_count += 1

# print(f"Your word {search_word} come {search_count} times in our paragraph")

### Practices ###

##Problem -> 1 Palindrome 

text_1 = input("Enter the text : ")

text_2 = text_1 [ ::-1]

if text_1 == text_2 :
    print(" Palindrome ")

else :
    print("Not a palindrome ")

##Problem  -> 2 Reverse Without Slicing

text_1 = input(" Enter the text : ")

text_2 = ""
num = len(text_1) - 1

for char in text_1:
    text_2 += text_1[num]
    num -= 1

if text_1 == text_2 :
    print(" Palindrome ")

else :
    print("  Not a palindrome  ")

print(text_1)
print(text_2)

##Problem ->  3 Count Vowels

text = input("Enter your text : ").lower()

vowels = "aeiou"

count = 0

for char in text :
    if char in vowels:
        count +=1

print(f"There are {count} Vowels in given text")

##Problem -> 4 Character Frequency

word = input("  Enter your word :  ")

character = input(" Enter Character you want to count : ")

count = 0

for char in word :
    if char == character:
        count += 1

print(f"{character} comes {count} times ")

##Problem -> 5 Remove Spaces 

text = input("Enter tha text : ")

result = ""

for char in text:
    if char == " ":
        continue
    result += char

print(result)

################# Challenge ####################

name = input("Enter your full name : ").lower().strip()

dob = input("Enter your birth year : ")

username = ""

for char in name:
    if char == " ":
        continue
    username +=char

username += dob

print("Your user name in : ", username) 

