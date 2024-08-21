# Author: <Jacqueline Guimac >
# Assignment / Part: HW3 - Q2 (etc.)
# Date due: 2023-06-12
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct. 

def avg_density(rock_measurements):
    if not rock_measurements:
        return 0.0

    total_density = 0.0
    total_rocks = len(rock_measurements)

    for rock in rock_measurements:
        density = rock[1]
        total_density += density

    average_density = total_density / total_rocks
    return round(average_density, 2)

# def main():
#     rocks = [("Granite", 2.63), ("Limestone", 2.71),("Sandstone", 2.32)] 
#     print(avg_density(rocks)) 

#     rocks = []
#     print(avg_density(rocks))
# main()
