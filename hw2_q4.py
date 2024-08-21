# Author: <Jacqueline Guimac>
# Assignment / Part: HW2 - Q4
# Date due: 2023-06-05
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct

max_value = int(input("Please enter a positive intger: "))
count_even_odd = 0 

for num in range(1,max_value+1):
    num_str = str(num)
    count_even_odd = 0 
    for i in num_str:
        if int(i)%2==0:
            count_even_odd += 1
        else:
            count_even_odd -= 1
    if count_even_odd > 0:
        print(num,end=' ')