# Author: <Jacqueline Guimac>
# Assignment / Part: HW2 - Q5a
# Date due: 2023-06-05
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import math 

length = int(input("Please enter the length of the sequence: "))
print("Please enter your sequence: ")
sequence = []
for i in range(length):
    num= float(input())
    sequence.append(num)
product = 1
for num in sequence:
    product *= num
geometric = math.pow(product,1/length)
geometric = round(geometric,4)
print("The geometric mean is:",geometric)