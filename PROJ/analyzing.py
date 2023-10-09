from alp_dict import create_double_dict 
from alp_dict import create_dict
from cleantext import clean
import matplotlib.pyplot as plt
import itertools
from itertools import islice


alp_dict = create_double_dict()
single_alp_dict = create_dict()


#print(alp_dict)

#print(single_alp_dict)

with open('readme.txt', 'r') as f:
    lines = f.readlines()


for each_line in lines:
    word_list = each_line.split()
    
    for each_word in word_list:

        character_list=[]
        for each_character in each_word:
            character_list.append(each_character)
        

        counter=0
        while counter< len(character_list)-1:
            
            double_character= character_list[counter] + character_list[counter+1]
            if double_character in alp_dict:
                alp_dict[double_character] = alp_dict[double_character] + 1
            counter = counter + 1

        for each_letter in each_word:
            if each_letter.isalpha():
                single_alp_dict[each_letter] = single_alp_dict[each_letter] + 1
            
print(single_alp_dict)
print(alp_dict)
#new_single_dict= {}
#new_list=sorted(single_alp_dict, key=single_alp_dict.get, reverse=True)

#for a in new_list:
#    new_single_dict[a] = single_alp_dict[]

#print(new_list)


#data = single_alp_dict
#names = list(data.keys())
#values = list(data.values())


#plt.bar(range(len(data)),values,tick_label=names)
#plt.savefig('bar.png')
#plt.show()

sortedlist = sorted(alp_dict.items(), key=lambda x:x[1])
sorteddict = dict(sortedlist)
lsorteddict = {}
for key in reversed(sorteddict):
    lsorteddict[key] = sorteddict[key]



data = dict(itertools.islice(lsorteddict.items(), 25))
names = list(data.keys())
values = list(data.values())


plt.bar(range(len(data)),values,tick_label=names)
plt.savefig('bar.png')
plt.show()

sortedlist = sorted(single_alp_dict.items(), key=lambda x:x[1])
sorteddict = dict(sortedlist)
lsorteddict = {}
for key in reversed(sorteddict):
    lsorteddict[key] = sorteddict[key]



data = dict(itertools.islice(lsorteddict.items(), 26))
names = list(data.keys())
values = list(data.values())


plt.bar(range(len(data)),values,tick_label=names)
plt.savefig('bar.png')
plt.show()



#print(alp_dict)
#print(single_alp_dict)









#for each_line in lines:
 #   for each_first_character in each_line:
  #      for each_second_character in each_line:
   #         double_character = each_first_character + each_second_character
    #        print(double_character)
#
 #           if double_character in alp_dict:
  #              alp_dict[double_character] = alp_dict[double_character] + 1

            


        












