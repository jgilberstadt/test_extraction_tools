from csv import reader
from csv import writer
from scipy import stats
import csv
import argparse
import os
import numpy as np
import re
parser = argparse.ArgumentParser(description='')
parser.add_argument('namescsv')
parser.add_argument('readcsv')
parser.add_argument('chartcsv')
parser.add_argument('output1csv')
parser.add_argument('output2csv')
args = parser.parse_args()
namesfile = args.namescsv
readfile = args.readcsv
chartfile = args.chartcsv
outputfile1 = args.output1csv
outputfile2 = args.output2csv
current_directory = os.getcwd()
arr=[]
sums=[]
medium_sums=[]
male_array=[]
female_array=[]
#change array to 3d
arr_num=0
abs_sum=1259656.0
with open(namesfile, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        row_to_string = ''.join(row)
        medium_sum=0
        arr=[]
        medium_sums=[]
        row_to_string2 = row_to_string.split('-')[1]
        part_1 = row_to_string2.split('S')[0]
        part_2 = row_to_string2.split('S')[1]
        string_search = part_1 + "_S_" + part_2
        with open(readfile, 'r') as read_new_obj:
            new_csv_reader = reader(read_new_obj)
            for line in new_csv_reader:
                line_to_string = ''.join(line)
                if re.search(row_to_string, line_to_string):
                    with open(chartfile, 'r') as read_new_obj:
                        final_csv_reader = reader(read_new_obj)
                        for data in final_csv_reader:
                            data_to_string = ''.join(data)
                            if re.search(string_search, data_to_string):
                                #Change "Male" and "Female" to whatever values you want to isolate
                                if 'Male' in data_to_string:
                                    male_array.append(line_to_string)
                                elif 'Female' in data_to_string:
                                    female_array.append(line_to_string)
                                break
with open(outputfile1, 'w', newline='') as output_obj:
    my_writer=writer(output_obj)
    for q in male_array:
        print(q, file=output_obj)
with open(outputfile2, 'w', newline='') as output_obj:
    my_writer=writer(output_obj)
    for r in female_array:
        print(r, file=output_obj)




