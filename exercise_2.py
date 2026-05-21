#Assignment 1
from selectors import SelectSelector


def discount_program():
    is_member = False
    level1 = 100
    level2 = 200
    discount = 0

    price = input("Välkommen, köp något dyrt: ")
    price = float(price)
    if price > level1:
        print("Grattis! Du har avancerat till nivå 1 och får 10% rebat.")
        discount = discount + 10

    if price >= level2:
        print("Grattis! Du har avancerat till nivå 2 och får 25% rebat.")
        discount = discount + 25

    if is_member:
        print("Som medlem får du extra 5% rabatt.")
        discount = discount + 5



    final_price = price * (100 - discount) / 100
    print(f"Efter rebatter blir priset... {final_price:.2f} kr \n\n")


#-------------------------------------------------------------

#Assignment 2 - To ride Balder at Liseberg you must be 130 cm tall. Write a program that can tell you if you can ride!

def height_program():
    is_member = False
    level1 = 100
    level2 = 200
    person_height = float(input("Enter you height in cm : "))

#Checking the condition with if statement
    if person_height >= 130:
        print("Your are allowed to ride")
    else:
        print("Your are not allowed to ride \n\n")


#-------------------------------------------------------------

#Assignment 3 -  program that asks the user how many goals each team scored, and tells which team won.

def championship_league():
    print(" Tottenham & Liverpool - championship League")
    print("Lets find out the winner based on their goals")

    tottenham = int(input("Tottenham goals in total :  "))
    liverpool = int(input("Liverpool goals in total :  "))

#calculate won by how many goals
    # abs is used for absolute value of number - it removes the (-) sign and only gives + number
    goals_ahead = abs(tottenham - liverpool)

#comparison of goals with if - to fine who won or draw

    if tottenham > liverpool:
        print("Tottenham won the match")
        print(f"Tottenham won by {goals_ahead} goals")

    elif tottenham == liverpool:
        print("It's draw / tie match")
        print(f"Both the team has {tottenham} goals")

    else:
        print("Liverpool won the match")
        print(f"Liverpool won by {goals_ahead} goals")


#-------------------------------------------------------------

# Assignment 4 - Write a program that can convert a temperature in degrees Celsius to degrees Fahrenheit.

def temp_conversion():

#Celsius to Fahrenheit

    C_celsius = float(input("Enter a temperature in Celsius : "))
    fahrenheit = 1.8 * C_celsius + 32
    print(f"It is {fahrenheit:.3f} Fahrenheit \n")

# Fahrenheit to Celsius
    F_fahrenheit = float(input("Enter a temperature in Fahrenheit : "))
    celsius = (F_fahrenheit - 32) / 1.8
    print(f"It is {celsius:.3f} Celsius \n")

# User choice of entering the temperature
    temp_choice = input("You want to enter the temperature in Fahrenheit or Celsius - Enter F or C) \n")

    if temp_choice == "F":
        fahrenheit_F = float(input("Enter a temperature in Fahrenheit : "))
        celsius_C = (fahrenheit_F - 32) / 1.8
    print(f"It is {celsius_C:.3f} Celsius")

    elif temp_choice == "C":
            celsius_C1 = float(input("Enter a temperature in Celsius : "))
            fahrenheit_F1 = 1.8 * celsius_C1 + 32
         print(f"It is {fahrenheit_F1:.3f} Fahrenheit")

















































"""
#Choose which program to run
program_to_run = input("Choose a program to run (1/2) : ")
if program_to_run == "1":
    discount_program()
elif program_to_run == "2":
    height_program()
"""
