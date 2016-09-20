import glob

#Custom key function for sorting
import re
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


for files in sorted(glob.glob("data.*.csv"), key=numericalSort):
    print files
