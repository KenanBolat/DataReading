

"""
Purpose: MGM Ground Observation Read Routines from daily multiple csv files
Author : Kenan BOLAT
"""

import datetime
import csv
import os
import datahandle

start = datetime.datetime.now()
print start




# Define Path
data_path = r"I:\temp\DailyGroundObservations\DailyGroundObservations"
merged_file = []

# Trace each file and replace "|"  with tab and "NULL" with 9999
for r,d,f in os.walk(data_path):
    print d
    for i in f:
        filename = os.path.join(r, i)
        file_tags = datahandle.Handle.get_file_tags(filename)
        datahandle.Handle.write_data(file_tags[1])










end = datetime.datetime.now()
print end-start