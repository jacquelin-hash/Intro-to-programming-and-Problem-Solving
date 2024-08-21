# Author: <Jacqueline Guimac >
# Assignment / Part: HW3 - Q5 (etc.)
# Date due: 2023-06-12
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct. 

def combine_weather_data(temperatures, precipitations):
    combined_data = []

    for i in range(len(temperatures)):
        temp = temperatures[i]
        precipitation = precipitations[i]
        data = "Temperature: {}°C, Precipitation: {} mm".format(temp, precipitation)
        combined_data.append(data)
    return combined_data


