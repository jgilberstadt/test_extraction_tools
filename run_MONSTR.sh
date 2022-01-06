#!/bin/bash
######## Job Name: Sample_Job ########
#SBATCH -J Sample_Job
######## Job Output File: Sample_job.oJOBID ########
#SBATCH -o /home/gilberstadt.j/Upload_from_Local/run_MONSTR_jobs/Sample_job.o%j
######## Job Error File: Sample_job.eJOBID ########
#SBATCH -e /home/gilberstadt.j/Upload_from_Local/run_MONSTR_jobs/Sample_job.e%j
######## Email
#SBATCH --mail-user=gilberstadt.j@wustl.edu
#SBATCH --mail-type=END,FAIL,TIME_LIMIT
######## Number of nodes: 1 ########
#SBATCH -N 1
######## Number of tasks: 1 ########
#SBATCH -n 1
######## Memory per node: 200 MB ########
#SBATCH --mem 40G
######## Walltime: 30 minutes ########
#SBATCH -t 50:00:00
#SBATCH --threads-per-core 1
#SBATCH --cpus-per-task 2

module load afni
module load fsl
module load ants

bash /home/gilberstadt.j/Upload_from_Local/fsltest/MONSTR1.2.1/MONSTR.sh --t1 $1 --atlasdir /home/gilberstadt.j/Upload_from_Local/fsltest/MONSTR1.2.1/20211027_Tom_Share_Corrected_MASS_Templates --o /scratch/gilberstadt.j/ADNI_data/final_custom_MONSTR_12 --natlas 12
