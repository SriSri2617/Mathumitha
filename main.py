from exercise_2 import discount_program, height_program, championship_league

#Choose which program to run
print("1. Discount Program")
print("2. Height check to ride")
program_to_run = input("Choose a program to run (1/2/3) : ")
if program_to_run == "1":
    discount_program()
elif program_to_run == "2":
    height_program()
elif program_to_run == "3":
    championship_league()
else:
    print("Invalid input")