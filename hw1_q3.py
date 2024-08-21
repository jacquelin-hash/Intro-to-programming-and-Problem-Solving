"""
Assignment / Part: HW1 - Q3 (Penny Pinching)
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter number of coins: ")
users_quarters = int(input("Number of quarters: "))
users_dimes = int(input("Number of dimes: "))
users_nickles = int(input("Number of nickles: "))
users_pennies = int(input("Number of pennies: "))

users_quarters = users_quarters * 25
users_dimes = users_dimes * 10
users_nickles = users_nickles * 5
users_pennies = users_pennies * 1

total_cents = users_quarters + users_dimes + users_nickles + users_pennies
dollar = total_cents // 100
reamining_cents = total_cents % 100

print("The total is " + str(dollar) + " dollar(s) and " + str(reamining_cents)+ " cent(s)")