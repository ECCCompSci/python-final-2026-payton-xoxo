# ============================================================
# Python Final Project 2026
# Name: Payton jones
# Date: 5/7/24
# Project Title: weather app
# Description: (Write 1-2 sentences explaining what your program does)
# ============================================================


# ---- SECTION 1: Setup / Variables ----
# Create your starting variables here.
# Example: player_name = ""



# ---- SECTION 2: Welcome Message ----
# Greet the user and explain what your program does.

print("Welcome!")
print("this program will tell the user about the tempature, whether they should bundle up, and how the wind affects it.  ")



# ---- SECTION 3: Get Input from User ----
# Use input() to ask the user for information.
# Remember: input() always returns a string.
# Use int() or float() if you need a number.
tempature = int(input("whats the tempature?"))
wind = int(input("whats the wind speed?"))
environment = input(" is it sunny, cloudy, snowy?")
sunny = print("Be ready it could get hotter !")
cloudy = print(" ooo it could get hotter or colder so be ready!")
snowy = print(" it probalby will get colder so bundle up!")
# Example
# player_name = input("What is your name? ")
# score = int(input("Enter a number: "))



# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.

# Example:
# if score >= 90:
#     print("Great job!")
# elif score >= 70:
#     print("Good work!")
# else:
#     print("Keep practicing!")
if tempature >= 70:
    print ("its warm")
elif tempature < 70:
    print("might want to grab a blanket..")

if wind >= 20:
    print("gonna be windy!")
elif wind < 20:
    print("might want to grab a blanket..")

if environment == sunny:
    print(sunny)

elif environment == cloudy:
    print(cloudy)

else:
    print(snowy)
# ---- SECTION 5: Final Output ----
# Print a final message, result, or summary to the user.

    print("hope you enjoy the weather!")
    print("Thanks for using my program!")
