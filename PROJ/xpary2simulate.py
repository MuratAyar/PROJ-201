import math

rightletters= { " ":[1.5,-4], "j":[-2,2], "u":[-1,2], "n":[0,2], "v":[1,2], "q":[2,2], "c":[-1.5,0], "t":[-0.5,0], "e":[0.5,0], "w":[-1.5,0], "f":[-1.5,-2], "i":[-0.5,-2], "m":[-0.5,-2], "z":[-2.5,-2]}
leftletters = {" ":[-1.5,-4], 'x':[-2, 2], 'p':[-1,2],"a": [0,2], "r": [1,2], "y": [2,2], "d": [-1.5, 0], "o": [-0.5,0], "h":[0.5,0], "g": [1.5,0],"l": [2.5, 0], "b": [-0.5, -2], "s": [0.5, -2], "k": [1.5,-2] }

right_handed= []
left_handed = []
is_right= False
is_left= False
right_sum=0
left_sum=0

with open('readme.txt', 'r') as f:
    lines = f.readlines()

for each_line in lines:
    word_list = each_line.split()
    
    for each_word in word_list:
        for each_letter in each_word:
            if is_right:
                if each_letter in rightletters.keys():
                    right_sum += 1
            
            if is_left:
                if each_letter in leftletters.keys():
                    left_sum += 1

            if each_letter in rightletters.keys():
                right_handed.append(each_letter)
                is_right= True
                is_left= False

            if each_letter in leftletters.keys():
                left_handed.append(each_letter)
                is_left= True
                is_right=False
            
       
        left_handed.append(" ")
        right_handed.append(" ")



right_lenghts = 0
left_lenghts = 0

ram_x = 666
ram_y = 666
right_x= 0
right_y = 0
left_x = 0
left_y = 0

left_count=0
right_count=0

total_row_lenght= 0

for letter in right_handed:
    right_count+=1
    if ram_x == 666:
        ram_x= rightletters[letter][0] 
    
    elif ram_x != 666:
        right_x = (rightletters[letter][0] - ram_x)**2

    if ram_y == 666:
        ram_y= rightletters[letter][0] 
    
    elif ram_y != 666:
        right_y = (rightletters[letter][0] - ram_y)**2
    
    a = math.sqrt(right_x + right_y)
    right_lenghts += a

    total_row_lenght += math.sqrt(ram_x**2 + ram_y**2)

for letter in left_handed:
    left_count+=1
    if ram_x == 666:
        ram_x= leftletters[letter][0] 
    
    elif ram_x != 666:
        left_x = (leftletters[letter][0] - ram_x)**2

    if ram_y == 666:
        ram_y= leftletters[letter][0] 
    
    elif ram_y != 666:
        left_y = (leftletters[letter][0] - ram_y)**2
    
    a = math.sqrt(left_x + left_y)
    left_lenghts += a


total_lenghts= right_lenghts + left_lenghts
print("total distance=" + str(format(total_lenghts, ".2f")))
print("right=" + str(right_count) + " | consecutive right=" + str(right_sum) + " | right ratio ="+ str(format(right_sum/right_count, ".2f")))
print("left=" + str(left_count) + " | consecutive left=" + str(left_sum) + " | left ratio =" + str(format(left_sum/left_count, ".2f")))
print("Homerow distance score = " + str(format(total_row_lenght, ".2f")))
