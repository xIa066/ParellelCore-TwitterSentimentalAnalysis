# ParellelCore-TwitterSentimentalAnalysis

# Objective
The task in this programming assignment is to implement a simple, parallelized application leveraging the University of Melbourne HPC facility SPARTAN. 
The application will use a 14 GB Twitter dataset , a grid/mesh for Melbourne map and a simple dictionary of terms related to sentiment scores. 
The objective is to calculate the sentiment score for the given cells and hence to calculate the area of Melbourne that has the happiest/most miserable people!

# Configuration
1. ssh log in SPARTAN by using unimelb/guest credentials

2. make a symbolic link to twitter data files, i.e. you should run the following commands at the Unix prompt from your own user directory on SPARTAN:

ln –s /data/projects/COMP90024/bigTwitter.json 

ln –s /data/projects/COMP90024/smallTwitter.json 

ln –s /data/projects/COMP90024/tinyTwitter.json

However, this may not be applicable because the file on SPARTAN no longer exists. In this case, ssh and upload twitter file from this repository

3. run Slurm file.rft script file https://github.com/xIa066/ParellelCore-TwitterSentimentalAnalysis/blob/master/Slurm%20file.rtf

following the command in here

https://dashboard.hpc.unimelb.edu.au/job_submission/

# Result
in report, https://github.com/xIa066/ParellelCore-TwitterSentimentalAnalysis/blob/master/Cloud_Assign1_Report.pdf 
