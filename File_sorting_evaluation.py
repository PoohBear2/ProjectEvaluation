#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import pandas as pd

wsi_folder = "wsi"
partition_df = pd.read_csv("https://github.com/PoohBear2/project/blob/main/project/TechnicalDemonstration/data/partition.csv?raw=true")

for index, row in partition_df.iterrows():
    file_name = row["file_name"]
    partition_name = row["partition"]
    class_name = row["class_name"]

    partition_folder = os.path.join(wsi_folder, partition_name)
    class_folder = os.path.join(partition_folder, class_name)
    assert os.path.exists(wsi_folder), "wsi folder not found"
    assert os.path.exists(partition_folder), f"{partition_folder} not found"
    assert os.path.exists(class_folder), f"{class_folder} not found"

print("Folders created as expected")

