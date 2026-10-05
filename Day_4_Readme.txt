# 🐍 Day 4 — Python Strings

## 🎯 Goal

Learn how to work with strings effectively and understand how text processing works in Python.

Strings are extremely important in real-world development because **usernames, passwords, filenames, API data, JSON, database values, and text processing** all involve strings.

---

## 📚 Topics Covered

- Creating strings
- Single, double, and triple quotes
- String indexing
- Negative indexing
- String slicing
- Reversing strings
- String methods
- `upper()`
- `lower()`
- `title()`
- `capitalize()`
- `strip()`
- `replace()`
- `find()`
- `count()`
- `startswith()`
- `endswith()`
- `split()`
- `join()`
- f-strings
- String loops
- String conditions
- Basic text analysis

---

# 💻 Practice Programs

## 1. Character Access

Practice accessing specific characters using indexes.

```python
text = "PythonDeveloper"

print(text[0])
print(text[-1])
print(text[4])
print(text[:6])
print(text[-5:])
```

---

## 2. String Reverse

Reverse a string using slicing.

```python
text = "Python"

print(text[::-1])
```

Output:

```text
nohtyP
```

---

## 3. Case Converter

Convert text into:

- Uppercase
- Title Case
- Lowercase

```python
text = input("Enter text: ")

print(text.upper())
print(text.title())
print(text.lower())
```

---

## 4. Character Counter

Take a sentence and a character from the user and count how many times the character occurs.

```python
sentence = input("Enter a sentence: ")
character = input("Enter a character: ")

count = sentence.count(character)

print(f"{character} occurs {count} times.")
```

---

## 5. Word Counter

Use `split()` to count the number of words.

```python
sentence = input("Enter a sentence: ")

words = sentence.split()

print(f"Number of words: {len(words)}")
```

---

## 6. Simple Email Validator

Check whether an email:

- Contains `@`
- Contains `.`
- Does not start with `@`

```python
email = input("Enter your email: ")

if "@" in email and "." in email and not email.startswith("@"):
    print("Valid email")
else:
    print("Invalid email")
```

> This is only a basic learning exercise, not a production-grade email validator.

---

## 7. Password Checker

Check whether a password:

- Has at least 8 characters
- Contains a number
- Contains an uppercase letter

```python
password = input("Enter your password: ")

has_number = False
has_uppercase = False

for character in password:

    if character.isdigit():
        has_number = True

    if character.isupper():
        has_uppercase = True

if len(password) >= 8 and has_number and has_uppercase:
    print("Password is valid")
else:
    print("Password is invalid")
```

---

# 🚀 Mini Project — Text Analyzer

The main project for Day 4 is a **Text Analyzer**.

The program accepts a paragraph and analyzes its contents.

### It calculates:

- Number of characters
- Number of words
- Uppercase characters
- Lowercase characters
- Digits
- Spaces
- Vowels
- Consonants
- Most common word
- Occurrences of a searched word

### Example Input

```text
Python is a powerful programming language.
Python is used for backend development,
automation, data science and machine learning.
```

### Example Output

```text
========== TEXT ANALYSIS ==========

Characters: 119
Words: 19
Uppercase characters: 1
Lowercase characters: 96
Digits: 0
Spaces: 18
Vowels: 38
Consonants: 58

Most common word: Python
Occurrences: 2
```

---

# 🧠 Interview Problems

The following problems were solved during Day 4:

### 1. Palindrome

Check whether a string reads the same forward and backward.

Example:

```text
madam → Palindrome
python → Not a palindrome
```

### 2. Reverse Without Slicing

Reverse a string using a loop instead of:

```python
text[::-1]
```

### 3. Count Vowels

Count the total number of vowels in a string.

### 4. Character Frequency

Find how many times each character appears.

Example:

```text
banana

b → 1
a → 3
n → 2
```

### 5. Remove Spaces

Remove spaces from a string using a loop instead of `.replace()`.

---

# 🔥 Challenge — Username Generator

Build a username generator that asks for:

```text
Enter your full name:
Enter your birth year:
```

Example:

```text
Name: Gyanendra Tiwari
Birth year: 2004
```

Possible output:

```text
gyanendra_tiwari2004
```

### Requirements

The program should:

- Remove unnecessary spaces
- Convert the name to lowercase
- Replace spaces appropriately
- Add the birth year
- Generate a username
- Shorten the username if it exceeds 15 characters

---

# 📁 Suggested Folder Structure

```text
python-day-04/
│
├── README.md
│
├── character_access.py
├── string_reverse.py
├── case_converter.py
├── character_counter.py
├── word_counter.py
├── email_validator.py
├── password_checker.py
│
├── palindrome.py
├── reverse_without_slicing.py
├── vowel_counter.py
├── character_frequency.py
├── remove_spaces.py
│
├── username_generator.py
└── text_analyzer.py
```

---

# ✅ Day 4 Checklist

- [x] String creation
- [x] String indexing
- [x] Negative indexing
- [x] String slicing
- [x] Reverse using slicing
- [x] `upper()`
- [x] `lower()`
- [x] `title()`
- [x] `capitalize()`
- [x] `strip()`
- [x] `replace()`
- [x] `find()`
- [x] `count()`
- [x] `startswith()`
- [x] `endswith()`
- [x] `split()`
- [x] `join()`
- [x] f-strings
- [x] Character counter
- [x] Word counter
- [x] Email validator
- [x] Password checker
- [x] Text Analyzer
- [x] Palindrome
- [x] Reverse using a loop
- [x] Vowel counter
- [x] Character frequency
- [x] Remove spaces
- [x] Username Generator

---

# 🎯 Day 4 Completion Test

Without looking at your notes, build a **Text Analyzer** that accepts a paragraph and reports:

```text
Characters
Words
Vowels
Consonants
Uppercase letters
Lowercase letters
Spaces
Occurrences of a searched word
```

You should be able to combine:

```text
Strings
   +
Loops
   +
Conditions
   +
Input
   +
String Methods
   +
f-Strings
```

If you can build the project independently, **Day 4 is complete.** 🚀

---

# 📌 What I Learned

Today I learned how Python handles text and how to inspect, modify, search, split, join, and analyze strings.

The key concepts I practiced were:

```text
Indexing → Slicing → Methods → Loops → Conditions → Text Analysis
```

---

# 🚀 Next Step — Day 5

## Python Collections

Topics:

- Lists
- Tuples
- Sets
- Collection operations
- Iterating through collections
- Adding and removing elements
- Searching and sorting
- Student Marks Manager

These concepts will later become important when working with:

**JSON → APIs → Databases → Backend Development → Real Python Applications**

---

## 👨‍💻 Author

**Gyanendra Tiwari**

Learning Python step by step and building practical projects. 🐍🚀