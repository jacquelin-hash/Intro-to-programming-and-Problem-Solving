"""
Assignment / Part: HW1 - Q4 (Mad as a Hatter, Thin as a Dime)
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

print("Please enter your amount of dollars and cents, in two seperate lines.")

dollars = int(input())
cents = int(input())

total = (dollars * 100) + cents

quarters = total // 25
dimes = ((total % 25) // 10) 
nickles = ((total % 25) % 10) //5
pennies = ((total % 25) % 10) % 5

print(str(dollars) + " dollars and " + str(cents) + " cents are: " + str(quarters) + " quarters, " + str(dimes) + " dimes, " + str(nickles) + " nickles and " + str(pennies) + " pennies")

