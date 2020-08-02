import csv
import os

# Assign file to load to file path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign flie to save to file path
file_to_save = os.path.join("Analysis","election_analysis.txt")

#Use with statement to open the file as a text file.
with open(file_to_save,"w") as txt_file:
    # Write some data to the file
    txt_file.write("Hello World")

# Open election results file and read.
with open(file_to_load) as election_data:

    #Perform Analysis

    # The data we need to retrieve
    # 1. Total number of votes cast
    # 2. List of candidates who received votes
    # 3. Percentage of votes for each candidate
    # 4. Total number of votes for each candidate
    # 5. Winner of the election based on popular vote

    print(election_data)


