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
parser.add_argument('outputcsv')
args = parser.parse_args()
namesfile = args.namescsv
readfile = args.readcsv
outputfile = args.outputcsv
current_directory = os.getcwd()
arr=[]
sums=[]
medium_sums=[]
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
        with open(readfile, 'r') as read_new_obj:
            new_csv_reader = reader(read_new_obj)
            for line in new_csv_reader:
                line_to_string = ''.join(line)
                if re.search(row_to_string, line_to_string):
                    line_to_string2 = line_to_string.split(' ')[1]
                    session_number = line_to_string.split('_')[1]
                    float_number = float(line_to_string2)
                    if 'b' in session_number:
                        medium_sums.append(0)
                        arr.append(float_number)
                    elif 'm' in session_number:
                        session_number_m = session_number.split('m')[1]
                        float_number_m = float(session_number_m)
                        medium_sums.append(float_number_m)
                        arr.append(float_number)
            if (len(arr) > 1):
                slope=stats.linregress(medium_sums,arr)
                slope_to_string=str(slope)
                cut1=slope_to_string.split(',')[0]
                cut2=cut1.split('=')[1]
                print(cut2)
                sums_entry=row_to_string + ", " + cut2
                print(sums_entry)
                sums.append(sums_entry)
with open(outputfile, 'w', newline='') as output_obj:
    my_writer=writer(output_obj)
    for q in sums:
        print(q, file=output_obj)
                    #else:
                        #session_number = line_to_string.split('m')[1]
                        #print(session_number)
