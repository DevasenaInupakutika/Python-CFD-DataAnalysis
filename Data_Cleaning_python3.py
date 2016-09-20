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

#Without using pandas
#Reading data from all the CSV files in ascending order of file names
#for files in sorted(glob.glob("data.*.csv"), key=numericalSort):
#    print files

#    with open(files, 'rb') as inf:
#        incsv = csv.reader(inf)
    
        #This skips the header of the CSV file.
#        next(incsv)

#        for row in incsv:
#            print row[0]


#Using Pandas
#Reading data from all the CSV files in ascending order of file names and creating a data frame with specified columns of csv files.
for files in sorted(glob.glob("data.*.csv"), key=numericalSort):
    
    files_wext = re.sub(r'\.csv$','', files) #File names without extension
    print(files)
    print(files_wext)

    data_df = pd.read_csv(files, sep=",", header=None, index_col=None)
    data2 = pd.concat([data_df[0], data_df[2], data_df[3], data_df[5], data_df[6]], axis=1)
    print(data2)
    np.savetxt(files_wext+'.dat', data2.values, fmt="%s")
