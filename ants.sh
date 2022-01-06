#!/bin/bash
######## Job Name: Sample_Job ########
#SBATCH -J Sample_Job
######## Job Output File: Sample_job.oJOBID ########
#SBATCH -o /home/gilberstadt.j/Upload_from_Local/ants_jobs/Sample_job.o%j
######## Job Error File: Sample_job.eJOBID ########
#SBATCH -e /home/gilberstadt.j/Upload_from_Local/ants_jobs/Sample_job.e%j
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

module load afni
module load fsl
module load ants

fullpath=$1
dirpath=$(dirname ${fullpath})
fname=$(basename ${fullpath})
fbase=$(echo ${fname} | rev | cut -f3- -d '.' | rev)

cd /scratch/gilberstadt.j/ADNI_data/final_ANTS

antsBrainExtraction.sh -d 3 -a $fullpath -e /home/gilberstadt.j/T_template.nii.gz -m /home/gilberstadt.j/T_templateProbabilityMask.nii.gz -o ${fbase}_
