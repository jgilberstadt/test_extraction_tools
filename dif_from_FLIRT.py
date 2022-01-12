#!/bin/bash
######## Job Name: Sample_Job ########
#SBATCH -J Sample_Job
######## Job Output File: Sample_job.oJOBID ########
#SBATCH -o /home/gilberstadt.j/Upload_from_Local/josh_vbm_bet_0_jobs/Sample_job.o%j
######## Job Error File: Sample_job.eJOBID ########
#SBATCH -e /home/gilberstadt.j/Upload_from_Local/josh_vbm_bet_0_jobs/Sample_job.e%j
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
parser.add_argument('flirtcsv')
parser.add_argument('outputcsv')
args = parser.parse_args()
namesfile = args.namescsv
readfile = args.readcsv
flirtfile = args.flirtcsv
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
        row_to_string = ''.join(row)
        medium_sums=[]
        medium_sum=0
        with open(readfile, 'r') as read_new_obj:
            new_csv_reader = reader(read_new_obj)
            for line in new_csv_reader:
                line_to_string = ''.join(line)
                with open(flirtfile, 'r') as read_flirt_obj:
                    flirt_csv_reader = reader(read_flirt_obj)
                    for name in flirt_csv_reader:
                        flirt_to_string = ''.join(name)
                        if re.search(row_to_string, line_to_string) and re.search(row_to_string, flirt_to_string):
                            line_to_string2 = line_to_string.split(' ')[1]
                            flirt_to_string2 = flirt_to_string.split(' ')[1]
                            float_number = float(line_to_string2)
                            flirt_number = float(flirt_to_string2)
                            dif = abs(float_number - flirt_number)
                            arr.append(dif)
                            print(dif)
        with open(outputfile, 'w', newline='') as output_obj:
            my_writer=writer(output_obj)
            for q in arr:
                print(q, file=output_obj)

