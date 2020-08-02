import csv
import os

# Assign file to load to file path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign flie to save to file path
file_to_save = os.path.join("Analysis","election_analysis.txt")

#Use with statement to open the file as a text file.
#with open(file_to_save,"w") as txt_file:
    # Write some data to the file
    #txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

# Initialize total vote counter
total_votes = 0

# Initialize candidate options list
candidate_options = []

# Declare candidate votes dictionary
candidate_votes = {}


# Open election results file and read.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read and print header row.
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        # Total vote count
        total_votes += 1

        # Candidate name
        candidate_name = row[2]
        # If a candidate is not in the options...
        if candidate_name not in candidate_options:
            # Add the name to the options list
            candidate_options.append(candidate_name)
            # Start tracking candidate votes
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    # The data we need to retrieve
# Total number of votes cast
print(total_votes)
# List of candidates who received votes
print(candidate_options)
# Total number of votes for each candidate
print(candidate_votes)
# Percentage of votes for each candidate
for candidate_name in candidate_votes:
    # Retreive vote count for each candidate
    votes = candidate_votes[candidate_name]
    # Calculate percentage of votes.
    vote_percentage = float(votes)/float(total_votes)*100
    # Print candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
# Winner of the election based on popular vote

    #print(election_data)


