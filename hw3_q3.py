# Author: <Jacqueline Guimac >
# Assignment / Part: HW3 - Q3 (etc.)
# Date due: 2023-06-12
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct. 

import math

def approximate_pi(num_of_terms):
    pi = 0
    denominator = 1
    sign = 1

    for i in range(num_of_terms):
        term = sign / (denominator * (3 ** i))
        pi += term
        sign *= -1
        denominator += 2

    pi *= math.sqrt(12)
    return pi


