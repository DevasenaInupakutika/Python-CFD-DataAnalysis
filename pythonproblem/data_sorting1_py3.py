#import os
# This is the path where all the files are stored.
#folder_path = 'c:\\'

# Open one of the files,
#for data_file in sorted(os.listdir(folder_path)):
#    print data_file

import csv
import glob
import pandas as pd
import numpy as np
#Custom key function for sorting
import re
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

#Using Pandas
#Reading data from all the CSV files in ascending order of file names and creating a data frame with specified columns of csv files.
for files in sorted(glob.glob("volume.*.csv"), key=numericalSort):
    
    files_wext = re.sub(r'\.csv$','', files) #File names without extension
    print(files)
    print(files_wext)

    data_df = pd.read_csv(files, sep=",", header=None, skiprows=[0])
    #print data_df
    data2 = pd.concat([data_df[0], data_df[1], data_df[2], data_df[3], data_df[4], data_df[5], data_df[6]], axis=1)
    #print data2
    np.savetxt(files_wext+'.dat', data2.values, fmt="%s")

#Merging created .dat files into a single final_volume.dat file
with open('final_volume.dat','w') as outfile:
    for files in sorted(glob.glob("volume.*.dat"), key=numericalSort):
    
        files_wext = re.sub(r'\.dat$','', files) #File names without extension
        print(files)
        print(files_wext)

        with open(files) as infile:
    	    for line in infile:
    		    outfile.write(line)
