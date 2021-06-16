
# * Hello World
# print("Hello World")

# * Drawing a Shape
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

# * Variables & Data Types
# character_name = "Tom"
# character_age = 50
# is_Male = False
# print(f"There once was a man named {character_name}, ")
# print(f"he was {character_age} years old. ")
# character_name = "Mike"
# print(f"He really liked the name {character_name}")
# print(f"but didn't liked being {character_age}.")

# * Working With Strings
# phrase = "freeCodeCamp"
# print(phrase.replace("Code","Programming"))

# * Working with Numbers
# from math import *

# my_num = -5
# print(sqrt(36))

# * Getting Input from Users
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"Hello {name}!")

# * Building a Basic Calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

# * Mab libs Game
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")

# print(f"Roses are {color}")
# print(f"{plural_noun} are blue")
# print(f"I love {celebrity}")

# * Lists
# friends = ["Kevin", "Karen", "Jim","Oscar", "Toby"]
# friends[1] = "Mike"
# print(friends[1])

# * List Functions
# lucky_numbers = [42, 8, 15, 16, 23]
# friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]
# friends2 = friends.copy()
# print(friends2)

# * Tuples
# coordinates = [(4, 5),(6,7),(80,34)]
# coordinates[1] = 10
# print(coordinates[0])

# * Functions
# def say_hi(name,age):
#     print(f"Hello {name} your are {age}")

# say_hi("Steve",35)
# say_hi("Mike",70)

# * Return Statement
# def cube(num):
#     return num ** 3

# result = cube(4)
# print(result)

# * If statements
# is_male = False
# is_tall = True

# if is_male and is_tall:
#     print("You are tall male")
# elif is_male and not is_tall:
#     print("You are a short mal")
# elif not is_male and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You are not a male and not tall")

# * If Statemtents & Comparisons
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max_num(300,4,5))

# * Building a better Calculator
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operator")

# * Dictionaries
# monthConversion = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }
# print(monthConversion.get("Luv", "Not a valid Key"))

# * While loops
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print("Done with loop")

# * Bassic guessing game
# secret_word = "code"
# guess = str()
# guess_count = 0
# guess_limit = 3
# guesses = True

# while guess != secret_word and guesses:
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         guesses = False

# if not guesses:
#     print("You lose")
# else:
#     print("You win!")

# * For loop
# friends = ["Jim","Karen","Kevin"]
# for index in range(5):
#     if index == 0:
#         print("first Iteration")
#     else:
#         print("Not first")

# * Exponent Function
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for _ in range(pow_num):
#         result *= base_num
#     return result

# print(raise_to_power(2,3))

# * 2D Lists & Nested Loops
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]

# for row in number_grid:
#     for col in row:
#         print(col)

# * Building a Translator
# def translate(phrase):
#     translation = str()
#     for letter in phrase:
#         if letter.lower() in "aeoiou":
#             if letter.isupper():
#                 translation += "G"
#             else:
#                 translation += "g"
#         else:
#             translation += letter
#     return translation

# print(translate(input("Enter a phrase: ")))

# * Comments
# print("Comments are fun")

# * Try / Except
# try:
#     answer = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid input")

# * Reading files
# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()

# * Writing to Files
# employee_file = open("index.html", "w")
# employee_file.write("<p>This is HTML</p>")
# employee_file.close()

# * Modules & Pip
# import useful_tools
# print(useful_tools.roll_dice(10))

# * Classes & Objects
# from Student import Student
# student1 = Student("Jim", "Business", 3.1, False)
# student2 = Student("Pam", "Art", 2.5, True)
# print(student1.name)

# * Building a Multiple Choice Quiz
# from Question import Question

# question_prompts = [
#     "What color are apples\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What color are strawberries\n(a) Yellow\n(b) Red\n(c) Bue\n\n"
# ]
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b"),
# ]


# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print(f"You got {score}/{len(questions)} correct")


# run_test(questions)

# * Object Functions
# from Student import Student

# student1 = Student("Oscar", "Accounting", 3.1)
# student2 = Student("Phyllis", "Business", 3.8)

# print(student1.on_honor_roll())

# * Inheritance
# from Chef import Chef
# from ChineseChef import ChineseChef

# myChef = Chef()
# myChef.make_chicken()

# myChineseChef = ChineseChef()
# myChineseChef.make_special_dish()
