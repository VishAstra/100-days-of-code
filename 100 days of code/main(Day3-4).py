#-----------------------------Conditional flow-------------------------------------
#       "=" ">>assignment == >> Check equality
# print("Welcome to the Rollercoater!!")
# height=int(input("Enter your height in cm:"))
# if height>=120:
#     print("You can ride the rollercoaster")
# else:
#     print("sorry, you have to grow taller")

#------------------------DAY-3.1 Exercise🤸 Odd or Even excecise------------
# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line
# if number%2==0:
#  print("number is even")
# else:
#  print("Number is odd")
#------------------------------nested if---------------------------------
# print("Welcome to the Rollercoater!!")
# height=int(input("Enter your height in cm:"))
# if height>=120:
#     print("You can ride the rollercoaster")
#     age=int(input("Enter Your age: "))
#     if age<=18:
#         print("please pay $7")
#     else:
#         print("Please pay $10")
# else:
#  print("sorry, you have to grow taller")
#------------------------------elif---------------------------------
# print("Welcome to the Rollercoater!!")
# height=int(input("Enter your height in cm:"))
# if height>=120:
#     print("You can ride the rollercoaster")
#     age=int(input("Enter Your age: "))
#     if age<12:
#         print("please pay $7")
#     elif age<=18:
#         print("please pay $7")
#     else:
#         print("Please pay $12")
# else:
#  print("sorry, you have to grow taller")
#------------------------DAY-3.2 Exercise🤸 BMI calculator 2.0------------
# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi=weight/(height*height)
# bmiround=round(bmi,2)
# if bmi<18.5:
#   print(f"Your bmi is {bmiround} and you are underweight")
# elif bmi<25:
#   print(f"Your bmi is {bmiround} and you are normal weight")
# elif bmi<30:
#   print(f"Your are bmi is {bmiround} and you are overwight")
# elif bmi<35:
#   print(f"Your are bmi is {bmiround} and you are obese")
# else:
#   print(f"Your bmi is {bmiround} and you are clinically obese")
#------------------------DAY-3.3 Exercise🤸 leap year------------
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

#Write your code below this line 👇


# if year %4==0:
#   if year%100==0:
#     if year%400==0:
#       print("leap year")
#     else:
#      print("not leap year")
#   else:
#    print("leap year")
# else:
#   print("Year is not a leap year")
#---------------------Multiple ℹ️f statement in succession-----------------------------
# print("Welcome to the Rollercoater!!")
# bill=0
# height=int(input("Enter your height in cm:"))
# if height>=120:
#     print("You can ride the rollercoaster")
#     age=int(input("Enter Your age: "))
#     if age<12:
#         bill=5
#         print("Children tickets are $5")
#     elif age<=18:
#         bill=7
#         print("Youth tickets are $7")
        
#     else:
#         bill=12
#         print("Adults tickets are $12")
#     wants_photos=input("do you want photos? Y or N : ")
#     if wants_photos=="Y":
#       bill +=3

#     print(f"Your final bill is {bill} ")  
    
# else:
#  print("sorry, you have to grow taller")
#------------------------DAY-3.3 Exercise🤸 Pizza order------------
# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bill=0
# if size=="S":
#     bill+=15
# elif size=="M":
#     bill+=20
# else:
#     bill+=25

# if add_pepperoni=="Y":
#     if size=="S":
#      bill+=2
#     else:
#      bill+=3

# if extra_cheese=="Y":
#   bill+=1
# print(f"Your bill is ${bill}")
#---------------------💡Logical Operator💡----------------------------

# print("Welcome to the Rollercoater!!")
# bill=0
# height=int(input("Enter your height in cm:"))
# if height>=120:
#     print("You can ride the rollercoaster")
#     age=int(input("Enter Your age: "))
#     if age<12:
#         bill=5
#         print("Children tickets are $5")
#     elif age<=18:
#         bill=7
#         print("Youth tickets are $7")
#     elif age>= 45 and  age<=55:
       
#        print("Your tickets are $0, Have a free ride on us")
       
      
#     else:
#         bill=12
#         print("Adults tickets are $12")
#     wants_photos=input("do you want photos? Y or N : ")
#     if wants_photos=="Y":
#       bill +=3

#     print(f"Your final bill is {bill} ")  
    
# else:
#  print("sorry, you have to grow taller")
#------------------------DAY-3.4 Exercise🤸 Love 💖Caluculator------------
# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# # #-------------------(eg sentence = 'Mary had a little lamb'
# # a=sentence.count('a')
# # print(a)
# # "Kilometer".lower()
# name_3=name1 +" " +name2
# name3=name_3.lower() ----------------

# t=name3.count('t')
# r=name3.count('r')
# u=name3.count('u')
# e=name3.count('e')
# true=t+r+u+e

# l=name3.count('l')
# o=name3.count('o')
# v=name3.count('v')
# e=name3.count('e')
# love=l+o+v+e

# ls=str(true)+str(love)
# love_score=int(ls)

# if love_score<10 or love_score>90:
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >=40 and love_score<=50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#    print(f"Your score is {love_score}")

# ------------------------DAY-3. Project🤸 🪙Treasure Island🏝️------------
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 

# left_right=input('You\'re at a cross road. Where do you want to go? Type "left" or "right" ').lower()
# if left_right=="left":
#     swim_or_wait=input('You\'ve come to a lake. There is an island in the middle of the lake.Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()
#     if swim_or_wait=="wait":
#         colour=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?: ").lower()
#         if colour=="yellow":
#              print("You Win")
#         elif colour=="red":
#             print("game over")
#         elif colour=="blue":
#              print("Game over")
#         else:
#            print("You chose the wrong door, Game over")
#     else:
#      print("Game Over")

# else:
#   print("Game Over")

#*****************************random module******************

import random
random_integer=random.randint(1,10)
print(random_integer)