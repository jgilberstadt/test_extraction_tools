#!/bin/bash
######## Job Name: Sample_Job ########
#SBATCH -J Sample_Job
######## Job Output File: Sample_job.oJOBID ########
#SBATCH -o /home/gilberstadt.j/Upload_from_Local/temp_ICV_jobs/Sample_job.o%j
######## Job Error File: Sample_job.eJOBID ########
#SBATCH -e /home/gilberstadt.j/Upload_from_Local/temp_ICV_jobs/Sample_job.e%j
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

module load fsl
module list

volume=$(fslstats /home/gilberstadt.j/Upload_from_Local/MNI152_T1_2mm_brain.nii.gz -V | cut -f2 -d ' ')

for fullpath in $(cat $1);
do	
	fbase=$(echo ${fullpath} | rev | cut -f2- -d '_' | rev)
	fmat=/scratch/gilberstadt.j/ADNI_data/skullstripping/FLIRT/${fbase}_T1w.mat
	determinant=$(avscale $fmat | grep Determinant | cut -f3 -d ' ')
	ICV=$(bc -l <<< "${volume}/${determinant}")
	echo $fullpath $ICV >> FSL_FLIRT.csv
done
