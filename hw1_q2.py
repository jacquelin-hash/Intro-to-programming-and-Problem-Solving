"""
Author: [Jacqueline Guimac]
Assignment / Part: HW1 - Q2 (Some Have Gone and Some Remain)
Date due: 2023-02-09, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
print("Please enter a year greater than 2023: ")

year = int(input())

seconds_per_day = 86400
days_per_year = 365
seconds_in_a_year = seconds_per_day * days_per_year

years_following_2023 = year - 2023

remaining_seconds = seconds_in_a_year * years_following_2023
births = (remaining_seconds // 7)
deaths = (remaining_seconds// 15)
immigrant = (remaining_seconds// 42)
emigration = (remaining_seconds // 75)

current_population_2023 = 330109174
new_population = current_population_2023 + births + immigrant - deaths - emigration
print("The population in year", year, "will be", new_population)