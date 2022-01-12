#!/bin/bash
######## Job Name: Sample_Job ########
#SBATCH -J Sample_Job
######## Job Output File: Sample_job.oJOBID ########
#SBATCH -o /home/gilberstadt.j/Upload_from_Local/patient_difference_R_jobs/Sample_job.o%j
######## Job Error File: Sample_job.eJOBID ########
#SBATCH -e /home/gilberstadt.j/Upload_from_Local/patient_difference_R_jobs/Sample_job.e%j
######## Email
#SBATCH --mail-user=gilberstadt.j@wustl.edu
#SBATCH --mail-type=END,FAIL,TIME_LIMIT
######## Number of nodes: 1 ########
#SBATCH -N 1
######## Number of tasks: 1 ########
#SBATCH -n 1
######## Memory per node: 200 MB ########
#SBATCH --mem 5G
######## Walltime: 30 minutes ########
#SBATCH -t 02:00:00

#module load python
#source activate test_MRQy

from csv import reader
from csv import writer
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
#change array to 3d
arr_num=0
abs_sum=1259656.0
with open(namesfile, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        arr=[]
        row_to_string = ''.join(row)
        medium_sums=[]
        medium_sum=0
        with open(readfile, 'r') as read_new_obj:
            new_csv_reader = reader(read_new_obj)
            for line in new_csv_reader:
                line_to_string = ''.join(line)
                if re.search(row_to_string, line_to_string):
                    line_to_string2 = line_to_string.split(' ')[1]
                    float_number = float(line_to_string2)
                    arr.append(float_number)
            print(arr)
            if (len(arr) > 1):
                for i in arr:
                    small_sums=[]
                    sum = 0
                    for j in arr:
                        k = abs(i - j)
                        small_sums.append(k)
                    for m in small_sums:
                        sum = sum + m
                    medium_sums.append(sum)
                for p in medium_sums:
                    medium_sum = medium_sum + p
                    #divide by tri sum
                medium_sum = medium_sum/(len(medium_sums)*(len(medium_sums)-1))
                number_to_string = str(medium_sum)
                sums.append(number_to_string)
                #output to csv
with open(outputfile, 'w', newline='') as output_obj:
    my_writer=writer(output_obj)
    for q in sums:
        print(q, file=output_obj)
        #my_writer.writerow(number_to_string)



    

       # arr.append(row)
#with open(readfile, 'r') as read_obj:
   # csv_reader = reader(read_obj)
   # for row in csv_reader:
       # arr_to_string = ''.join(arr[arr_num])
       # row_to_string = ''.join(row)
       # if re.search(arr_to_string, row_to_string):
           # row_to_string2 = row_to_string.split(' ')[1]
           # float_number = float(row_to_string2)
           # abs_sum = abs(abs_sum - float_number)
           # print(abs_sum)
