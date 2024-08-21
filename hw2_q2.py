# Author: <Jacqueline Guimac>
# Assignment / Part: HW2 - Q2
# Date due: 2023-06-05
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

# non_modified_string = input("Enter a string to modify: ")
# two_characters = input("Enter two characters separated by a space: ")
string_to_modify = input("Enter the string to modify: ")
replacement = input("Enter the characters for replacement (separated by a space): ")

old_characters =replacement[0]
new_characters = replacement[1]

modified_string = ""
for char in string_to_modify:
    if char == old_characters:
        modified_string+=new_characters
    else:
        modified_string += char

print("Your Modified string is:", modified_string)
