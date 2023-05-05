# Install and Setup

# REPL

# VSCode & Extension



# 1. Variables / Types
# my_age=31
# my_name="vishnu"
# my_wife="athira"
# print(f"hi, my name is { my_name} and I am {my_age}, my wifes's name is {my_wife}")

# Challenge 1 - Variables

# Python has a bunch of pre-made, built-in tools which you can use to perform tasks. 
# One is these tools is the input() function which allows us to retrieve a user input. 
# You can see these here, including the input() function: https://www.w3schools.com/python/python_ref_functions.asp

# Read about the input() function, try out the example to see how it works, and then only proceed.

# For this challenge, use this input function to ask “What is your favorite color?”. 
# Save the response into a variable named my_input. 
# Then print “Your favorite color is my_input”. 
# So if I type red as my favorite color, it will print “Your favorite color is red”. 


# # WORK OUT YOUR SOLUTION HERE
# my_input=input("What is your favorite color?")
# print("Your favorite color is"+" "+my_input)



# 2. Conditional Logic
# my_number=int(input("enter the number: "))
# if my_number > 5:
#     print("Your number is greater than")
# elif my_number<5 :
#     print("Your number is less than 5")
# else:
#     print("Your number is equal to 5")


# my_number=int(input("enter the number: "))
# if my_number>0 and my_number<10:
#     print("Your nunber is single digit")
# else:
#     print("your number is not single digit")


# Challenge 2 - Conditionals - Rock, Paper, Scissors

# We'll use what we've so far to create the Rock, Paper, Scissors game. Here's how:

# First, you'll need to capture inputs for both Player 1 and Player 2. 

# Next, you'll use conditionals to check the two answers and see who wins. This seems pretty
# complicated on the surface but don't overthink it. Here's some help: 
# If Player 1 plays Paper, then there are only two conditionals to check against (Rock, Scissors).
# This means for each element, there should be two checks, totalling 6 checks overall. Each check 
# should print "Player x wins" with the correct player based on the condition. 

# Finally, there should be a check for the same element being played, i.e. if both players play rock
# then an error message should be printed like "Error, you aren't allowed to play the same thing".

# WORK OUT YOUR SOLUTION HERE
# print("Welcome to Rock🪨, Paper🗞️  Scissors✂️ game")
# player_1=input("Hi, player1️⃣. Enter you input: ").lower()
# player_2=input("Hi, player2️⃣. Enter you input: ").lower()
# if player_1==player_2:
#     print("Error, you aren't allowed to play the same thing")
# elif player_1 =="rock" and player_2=="paper":
#     print("Player 2 wins")
# elif player_1 =="rock" and player_2=="scissors":
#     print("Player 1 wins")
# elif player_1 =="paper" and player_2=="rock":
#     print("Player 1 wins")
# elif player_1 =="paper" and player_2=="scissors":
#     print("Player 2 wins")
# elif player_1 =="scissors" and player_2=="rock":
#     print("player 2 wins")
# elif player_1 =="scissors" and player_2=="Paper":
#     print("player 1 wins")
# else:
#     print("Something went wrong, Please try again")





# 3. Lists
#1 lists
# birds=["Parrot", "bluebird", "Sparrow"]
# print(birds[1])
# print(birds[-1])

#2 sort
# birds=["Parrot", "Bluebird", "Sparrow"]
# birds.sort()
# print(birds)

#3 insert
# birds=["Parrot", "Bluebird", "Sparrow"]
# birds.insert(0, "crow")
# print(birds)

#3 slice not inclusive
# birds=["Parrot", "Bluebird", "Sparrow", "Peacock", "owl"]
# birds_slice=birds[1:4]
# print(birds_slice)
# birds=["Parrot", "Bluebird", "Sparrow", "Peacock", "owl"]
# birds_slice=birds[2:]
# print(birds_slice)
# Challenge 3 - Lists

# Find the solutions using this list

# birds = ["robin", "bluebird", "sparrow", "cardinal"]
# birds = ["robin", "bluebird", "sparrow", "cardinal"]
# bl=birds[1]
# print(bl)
# 1. Save "bluebird" in a variable

# WORK OUT YOUR SOLUTION HERE
# birds = ["robin", "bluebird", "sparrow", "cardinal"]
# # bl=birds[1]
# # print(bl)

# 2. Save "cardinal" in a variable
# birds = ["robin", "bluebird", "sparrow", "cardinal"]
# cardinal=birds[3]
# print(cardinal)
# WORK OUT YOUR SOLUTION HERE


# 3. Insert "woodpecker" directly behind sparrow in the list

# WORK OUT YOUR SOLUTION HERE
# birds = ["robin", "bluebird", "sparrow", "cardinal"]
# birds.insert(2,"woodpecker")
# print(birds)

# 4. Reverse the birds list and print it out

# WORK OUT YOUR SOLUTION HERE
# birds = ["robin", "bluebird", "sparrow", "cardinal"]
# birds.reverse()
# print(birds)

# 5. Save the first two birds only into a new variable called two_birds

# WORK OUT YOUR SOLUTION HERE
# birds = ["robin", "bluebird", "sparrow", "cardinal"]
# two=birds[0:2]
# print(two)

# 6. Print ["sparrow", "cardinal"] using negative indices

# WORK OUT YOUR SOLUTION HERE
# birds = ["robin", "bluebird", "sparrow", "cardinal"]
# print(birds[-2:])



# 4. Loops
#for loop🏆

# name ="Vishnu"
# for i in name:
#     print(i)

# numbers=[0, 2, 4, 6, 8, 10]
# for n in numbers:
#     n=n*2
#     print(n)
#*********while loo🏆
# counter = 0
# while counter < 12:
#  counter=counter + 1
#  print(counter)
# Challenge 4 - Loops

# items = ["steak", "apple", "bread", "butter", "pineapple"]


# 1. Write a 'for loop' that loops through the above list and prints "item is a fruit" or "item is not a fruit" depending on whether it is or not. 
#    Note that it should not say item but the name of the fruit. So 'steak is not a fruit', 'apple is a fruit', etc. 

# WORK OUT YOUR SOLUTION HERE

# items = ["steak", "apple", "bread", "butter", "pineapple"]
# for item in items:
#     if item=="apple" or item=="pineapple":
#         print( item +" is fruit")
#     else:
#        print(item+ " is not fruit")
        
# 2. Write a while loop starting with a counter = 1 that multiplies two to your counter, prints the counter, but breaks the loop after the counter reaches 1000. 


# WORK OUT YOUR SOLUTION HERE

# counter=1
# while counter < 1000:
#  counter *=2
#  print(counter)
# counter=1
# while True:
#    counter *= 2
#    print(counter)
#    if counter > 1000:
#          break

# 5. Functions
#function is a block of code that runs only when you call it
# 1️⃣def make_some_eggs():
#      print("New order for eggs")
# make_some_eggs()
# #2️⃣
# def make_some_eggs(egg_type):
#     print("new order for " + egg_type +" egg")
# make_some_eggs("boiled")

#3️⃣
# def make_some_eggs(quantity, egg_type):
#     print("new order for " +quantity +" "+ egg_type +" egg")
# make_some_eggs("6" , "boiled")
#4️⃣

# def counter(start, end):
#    counter =start
#    while counter <end:
#     counter=counter*2
#     print(counter)
# counter(1,1000)
# Challenge 5 - Functions

# Write a function that takes a list of numbers and prints a new list with only the numbers less than 10 in it.

# WORK OUT YOUR SOLUTION HERE

# def under_ten_list(list_of_numbers):
#     new_number=[]
#     for number in list_of_numbers:
#         if number<10:
#             new_number.append(number)
#     print(new_number)

# under_ten_list([1, 81, 45, 3, 9, 35, 87, 44, 6])

# def under_ten_list(list_of_number):
#  new_number=[]
#  for number in list_of_number:
#   if number <20:
#    new_number.append(number)
#  print(new_number)
# under_ten_list([18, 29, 9, 32, 14, 19 , 88, 99, 54])

#eg fruits=["apple", "pineapple"]
# fruits.append("orange")
# print(fruits)
# 6. Dictionaries>> key and values
# my_self=["Vishnu","Athira",31, "November"]
# my_self = {
#     "Name":"Vishnu",
#     "wife's name" :"Athira",
#     "age":31,
#     "month":"november"
# }
# print(my_self["Name"])

#2️⃣
# my_self = {
#     "Name":"Vishnu",
#     "wife's name" :"Athira",
#     "age":31,
#     "month":"november"
# }
# print(my_self.keys())

# my_self = {
#     "Name":"Vishnu",
#     "wife's name" :"Athira",
#     "age":31,
#     "month":"november"
# }
# print(my_self.values())

# my_self = {
#     "Name":"Vishnu",
#     "wife's name" :"Athira",
#     "age":31,
#     "month":"november"
# }
# print(my_self.items())
# for t in my_self.values():
#  print(t)
# Challenge 6 - Dictionaries

# college = {
#     "name": "Yale",
#     "founded": "1701",
#     "motto": "Light and truth",
#     "location": "New Haven, Connecticut",
#     "students": 12060
# }

# 1. Loop through dictionary and print all the values (values only)

# WORK OUT YOUR SOLUTION HERE
# college = {
#     "name": "Yale",
#     "founded": "1701",
#     "motto": "Light and truth",
#     "location": "New Haven, Connecticut",
#     "students": 12060
# }

# for i in college.values():
#  print(i)

# # 2. Loop through dictionary and print all the keys and values
# for i in college.items():
#  print(i)
# # WORK OUT YOUR SOLUTION HERE
# for i in college.items():
#  print(i)

# # 3. Print the "founded" year of the college
# print(college["founded"])
# # WORK OUT YOUR SOLUTION HERE




# FINAL PROJECT - Password Checker

# 1. Get password input
# 2. Check if password has lowercase, uppercase, a number, and a special character. 
# 3. If the password doesn't meet all four conditions, then reject with the conditions they still need to meet.
# 4. Only accept if all four conditions are met.
# 5. Add a condition to check that password length is greater than 9 digits. If 9 or less, it fails.

# Hints/Suggestions:
# - Break password into list of letters and loop through to check type (upper, lower, etc.). Check out
#   the Python string package for help with upper, lower, and digits. https://docs.python.org/3/library/string.html. Import this package by
#   putting 'import string' at the top of your file. This will import the library and give you access to its methods.
# - Consider creating a function or two to clean up any repetitiveness. 
# - Remember that there are many ways to complete this task. Many programmers will provide many different solutions. Some will
#   be more "efficient" or more "clean" than others. Who cares at this point. Find what solutions works for you AND successfully
#   checks passwords and call it a win!
# import string
# password=input("Enter the password: ")
# my_password_list=list(password)
# requirements=["uppercase", "lowercase", "digits", "special characters"]
# for char in my_password_list:
#     if char in string.ascii_uppercase:
#         if "uppercase" in requirements:
#          requirements.remove("uppercase")
#     elif char in string.ascii_lowercase:
#         if "lowercase" in requirements:
#          requirements.remove("lowercase")
#     elif char in string.digits:
#         if "digits" in requirements:
#          requirements.remove("digits")
#     else:
#         if "special characters" in requirements:
#           requirements.remove("special characters")
# if len(requirements)==0 and len(my_password_list)>9:
#    print("Your password is strong")
# if len(my_password_list)<=9:
#     print("Password length is short")
# if len(requirements)!=0:
#     print("Your password is not strong enough. The following requirements are not met: "+ " ,".join(requirements))




import re

def check_password(password):
    # Check password length
    if len(password) <= 9:
        return "Password must be at least 10 characters long."
    
    # Check for lowercase letter
    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter."
    
    # Check for uppercase letter
    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    
    # Check for number
    if not re.search("[0-9]", password):
        return "Password must contain at least one number."
    
    # Check for special character
    if not re.search("[^a-zA-Z0-9]", password):
        return "Password must contain at least one special character."
    
    # If all conditions are met, return success message
    return "Password accepted."

# Get password input from user
password = input("Enter your password: ")

# Check password using the function
result = check_password(password)

# Print result
print(result)
