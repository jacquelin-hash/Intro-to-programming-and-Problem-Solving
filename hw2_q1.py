# Author: <Jacqueline Guimac>
# Assignment / Part: HW2 - Q1
# Date due: 2023-06-05
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

print("Welcome to the Sports Score Tracker!")
num_matches = int(input("Enter the number of matches played: "))

total_score = 0

for match in range(1, num_matches + 1):
    score = int(input("Enter the score for match " + str(match) + ": "))
    total_score += score

average_score = total_score / num_matches
average_score = round(average_score,2)

print("Average score of the team:",average_score)