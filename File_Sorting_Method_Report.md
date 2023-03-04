
# Report for the File_sorting Method
#### Design Choices and Reasoning
1. The first two import statements are for the os and shutil modules, which are used for working with the file system, and the pandas module, which is used for working with tabular data. In order to download the github csv file as a raw file that can be processed, I added ?raw=true to the end of the url to signify this.
2. The code starts by checking if a folder named "wsi" exists, and creates it if it doesn't. This is to ensure that there is a folder where the whole slide images (WSIs) can be stored after they have been partitioned.
3. The code then loops through each row in the partition CSV file using the iterrows() method of the partition_df DataFrame. For each row, it extracts the file name, partition name, and class name. It then checks if a folder named after the partition exists in the "wsi" folder, and creates it if it doesn't. This is to ensure that there is a folder for each partition where the WSIs can be stored.
4. It then checks if a folder named after the class exists within the partition folder, and creates it if it doesn't. This is to ensure that there is a folder for each class within each partition where the WSIs can be stored.
5. Finally, it searches for the WSI file with the specified file name in the dataset that was downloaded from dropbox using the os.listdir() and os.path functions. Once it finds the file, it copies it to the correct partition and class folder using the shutil.copyfile() function. This is done for each row in the partition CSV file in order to sort each file into its proper directory.
6. I added a message at the end of the program in order to indicate that the partitioning process is complete. 

#### Performance Improvement Suggestions
The code that I created could better clarify its user input sections. such as an “insert here” string for the path to the dataset folder. This program could also be turned into a method that could be incorporated into the deepslide repository as a preprocessing procedure.

#### Model Evaluation and Analysis
To evaluate the program’s performance, a separate script titled “File_sorting_evaluation” verifies that the "wsi" folder is created through an os.path.exists assertion. The for index, row in partition_df.iterrows() loop iterates through each row in the partition DataFrame and retrieves the values for the "file_name", "partition", and "class_name" columns using row["file_name"], row["partition"], and row["class_name"]. The os.path.join() function is then used to join the "partition" and "class" folder names with the "wsi" folder name to create the full path for each folder. The assert statements then verify that each folder exists using os.path.exists() function. If any folder is not found, an assertion error is raised with a custom error message indicating which folder was not found. If all the folders are found, the code prints a message indicating that the folders have been created as expected. 
