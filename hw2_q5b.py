# Author: <Jacqueline Guimac>
# Assignment / Part: HW2 - Q5b
# Date due: 2023-06-05
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

import math
print("Please enter a non- empty sequence of positive integeres, each one on a seperate line. End your sequence by typing done.: ")
sequence = []
while True:
    num = input()
    if num == "done":
        break
    sequence.append(float(num))

product = 1
for num in sequence:
    product *= num

geometric_mean = math.pow(product, 1 / num)
geometric_mean = round(geometric_mean,4)
print("The geometric mean is: ",geometric_mean)
