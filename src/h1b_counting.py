# -*- coding: utf-8 -*-
"""h1b_counting.py

This program takes in different files that 
have H1-B records of certififcations and output 
specific statistics about the data. 

"""

# neccessary imports all within python standard library:
import io 
import sys
import os
import collections
from collections import OrderedDict
from collections import Counter
import operator


# below: loading in data from arguments 
file = open(sys.argv[1],'r') 
file1 = file.readlines()

print(len(file1))

big_list = []
for line in file1:
    currentline = line.split(";")
    big_list.append(currentline)

total_entry_number = len(file1) - 1
big_list[0][0] = 'INDEX'



def get_num(string):
    ''' 
    this is a funtion that gets 
    the index for a given column name
    '''
    for i in range(0,len(big_list[0])):
        #print(i," ",big_list[0][i])
        if big_list[0][i] == string:
            return i



LCA_CASE_SOC_NAME = get_num('LCA_CASE_SOC_NAME')
LCA_CASE_EMPLOYER_STATE = get_num('LCA_CASE_EMPLOYER_STATE')
STATUS = get_num('STATUS')

# for formats from documents 2016 and older
# the below  statements become neccessary

if get_num('STATUS') == None:
    STATUS = get_num('CASE_STATUS')
if get_num('LCA_CASE_SOC_NAME') == None:
    LCA_CASE_SOC_NAME = get_num('SOC_NAME')
if get_num('LCA_CASE_EMPLOYER_STATE') == None:
    LCA_CASE_EMPLOYER_STATE = get_num('EMPLOYER_STATE')


# --------------------
#   PREPEOCESSING:
# --------------------







big_status_list = []
for i in range(0,len(big_list)):
    big_status_list.append(big_list[i][STATUS])
print(len(big_status_list))

cert_dict = dict(Counter(item for item in big_status_list))
total_cert = cert_dict['CERTIFIED'] # this returns us the total value of all certifieds


#  OCCUPATIONS:

occ_name_list = []
for i in range(0,len(big_list)):
    occ_name_list.append(big_list[i][LCA_CASE_SOC_NAME])


occ_set = list(set(occ_name_list)) # this gives us unique occupation names

big_list_occ = []
for occ in occ_set:    
    occ_list = []
    for i in range(0,len(big_list)):
        if big_list[i][LCA_CASE_SOC_NAME] == occ:
            occ_list.append(big_list[i][STATUS]) # appending status
    big_list_occ.append((occ,occ_list)) # occupation along with a list of statuses

dict_big_occ = dict(big_list_occ)


list_mega_occ = []
for i in range(0,len(dict_big_occ)):
    key1 = list(dict_big_occ.keys())[i]
    tally = dict(Counter(item for item in list(dict_big_occ.values())[i]))
    list_mega_occ.append([key1, tally])



#  STATES :

    

state_name_list = []
for i in range(0,len(big_list)):
    state_name_list.append(big_list[i][LCA_CASE_EMPLOYER_STATE])


state_set = list(set(state_name_list))
print('got to here')

big_list_state = []
for state in state_set:    
    state_list = []
    for i in range(0,len(big_list)):
        if big_list[i][LCA_CASE_EMPLOYER_STATE] == state:
            state_list.append(big_list[i][2])
    big_list_state.append((state,state_list))

dict_big_state = dict(big_list_state)

list_mega_state = []
for i in range(0,len(dict_big_state)):
    key1 = list(dict_big_state.keys())[i]
    tally = dict(Counter(item for item in list(dict_big_state.values())[i]))
    list_mega_state.append([key1, tally])


#  --------------------------------------------------
#    SORTING FROM list of lists with dictionaries to 
#    single ORDERED DICTIONARIES:
#  --------------------------------------------------

# OCCUPATIONS:


for i in range(0,len(list_mega_occ)):
    #print(i)
    if 'CERTIFIED' not in list_mega_occ[i][1]:
        list_mega_occ[i][1]['CERTIFIED'] = 0

dict_occ = {}

for i in range(0,len(list_mega_occ)):
    dict_occ.update({list_mega_occ[i][0]:list_mega_occ[i][1]['CERTIFIED']})

dict_occ = OrderedDict(dict_occ)
sorted_dict_occ = sorted(dict_occ.items(), key=operator.itemgetter(1), reverse = True)


# STATES:


for i in range(0,len(list_mega_state)):
    #print(i)
    if 'CERTIFIED' not in list_mega_state[i][1]:
        list_mega_state[i][1]['CERTIFIED'] = 0

dict_state = {}
for i in range(0,len(list_mega_state)):
    dict_state.update({list_mega_state[i][0]:list_mega_state[i][1]['CERTIFIED']})

dict_state = OrderedDict(dict_state)
sorted_dict_state = sorted(dict_state.items(), key=operator.itemgetter(1), reverse = True)


print('got to here2')

# -----------
#   OUTPUT:
# -----------


# TOP OCCUPATIONS:

file_occ = open(sys.argv[2],'w') 

file_occ.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE') 
file_occ.write('\n')

for item in sorted_dict_occ[0:10]:
    percent_num = item[1]/total_cert
    percent = "%.1f" %percent_num 
    file_occ.write(str(item[0]).upper()+';'+str(item[1])+';'+str(percent)+'%')
    file_occ.write("\n")

 
file_occ.close() 

# TOP STATES:


file_state  = open(sys.argv[3], 'w') 


file_state.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE') 
file_state.write('\n')

for item in sorted_dict_state[0:10]:
    percent_num = item[1]/total_cert
    percent = "%.1f" %percent_num 
    file_state.write(str(item[0]).upper()+';'+str(item[1])+';'+str(percent)+'%')
    file_state.write("\n")

 
file_state.close() 








