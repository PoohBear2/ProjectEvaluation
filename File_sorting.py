#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Create the wsi directory with the data from the dataset properly sorted.
import os
import shutil
import pandas as pd

# check if wsi folder exists, if not create it
wsi_folder = "wsi"
if not os.path.exists(wsi_folder):
    os.mkdir(wsi_folder)

# read partition.csv
partition_df = pd.read_csv("https://github.com/PoohBear2/project/blob/main/project/TechnicalDemonstration/data/partition.csv?raw=true")

# loop through partition.csv
for index, row in partition_df.iterrows():
    file_name = row["file_name"]
    partition_name = row["partition"]
    class_name = row["class_name"]

    # create partition folder if it doesn't exist
    partition_folder = os.path.join(wsi_folder, partition_name)
    if not os.path.exists(partition_folder):
        os.mkdir(partition_folder)

    # create class folder if it doesn't exist within the partition folder
    class_folder = os.path.join(partition_folder, class_name)
    if not os.path.exists(class_folder):
        os.mkdir(class_folder)

    # find the file in the separate folder and copy it to the correct partition and class folder
    separate_folder = r"C:\Users\tzhou\Downloads\Slides"
    for sub_folder in os.listdir(separate_folder):
        sub_folder_path = os.path.join(separate_folder, sub_folder)
        if os.path.isdir(sub_folder_path):
            source_file_path = os.path.join(sub_folder_path, file_name)
            if os.path.exists(source_file_path):
                dest_file_path = os.path.join(class_folder, file_name)
                shutil.copyfile(source_file_path, dest_file_path)
print('All done!')

