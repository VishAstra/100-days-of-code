# Write your code below this line 👇
#---------------- DAY 1️⃣---------------------------
#---------------next line-------------------------
# print("Hello World\nHello World\nHello World")
# print("Hello" +" "+ "Vishnu")
# print('e.g. print("Hello" + "world")')
#---------length of a string--------------------
# s=input("what is your name:")
# print(len(s))
# print(len(input("what is your name: ")))
#------------input functions------------------------
# v=input("enter your name:")
# print ("Your name is " + v)
#--------eg:2
# print("Hello " + input("Enter Your name:"))
#----------Variables-----------------------
# a = input("a: ")
# b= input("b: ")

# c=a
# a=b
# b=c
# print("a: " + a)
# print("b: "  + b)
#-------project1 band generator---------------
# #1. Create a greeting for your program.
# print("Welcome to the Band Name Generator.")
# #2. Ask the user for the city that they grew up in.
# city=input("Enter the city that you grew up\n ")
# #3. Ask the user for the name of a pet.
# pet=input("Enter the name of your pet\n ")
# #4. Combine the name of their city and pet and show them their band name.
# print("Your band name is " + city + " " +pet)

#--------------------(Day 2️⃣)------------------------
#Data Types
#string eg of subscript
# print("hello"[0])
#------------------------------------------------------
#integer, Float and boolean(True/False)
# print(123+456)
# print(float(4/5))

#*len function does not work with integer
# print(type(4)) >>>to check the type
#eg 1️⃣----------------------------------------------
# num_char=len(input("Enter your name:\n"))
# print("you name has" + " "+str(num_char)+" characters")

#---------------------DAY2.1 excercise⛹️‍♀️------------
# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# first_digit=int(two_digit_number[0])
# second_digit=int(two_digit_number[1])
# result=first_digit+second_digit
# print(result)

#Mathmatical Expression➕➖➗🟰
#PEMDASLR (),**,

#------------------------DAY-2.2-exercise🤸 BMI Calculator------------
# # 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# h=float(height)
# w=float(weight)
# BMI= w/(h*h)
# print(int(BMI))

# Round a number 3 decimal places
# print(round(8/3,3))
# print(8//3)
#-------eg----------
# score=3
# score += 2
# print(score)

# f-string*******************(f"yourscore{}")
# score=input(("Enter your score:"))
# print(f"your score is : {score}")

# score=80
# grade="A"
# print(f"your score is: {score} and grade is {grade}")

#------------------------DAY-2.3 Exercise🤸 Life in Weeks------------
# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆

#Write your code below this line 👇
# age_as_int=int(age)
# years_remaining=90-age_as_int
# days=years_remaining*365
# weeks=years_remaining*52
# months=years_remaining*12
# print(f"You have {days} days, {weeks} weeks and {months} months left")
#------------------------DAY-2.4 Exercise🤸 Tip Calculator------------
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $ "))
tip=int(input("What percentage tip would you like to give? 10,12, or 15? "))
people=int(input("How many people split the bill ? "))
bill_with_tip=tip/100*bill+bill
bill_per_person=bill_with_tip/people
final_amount="{:.2f}".format(bill_per_person)
print(f"Each person should pay: $ {final_amount}")


