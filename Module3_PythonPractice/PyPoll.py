import csv
import os

# Assign file to load to file path
file_to_load = os.path.join("..","Resources","election_results.csv")

# Assign flie to save to file path
file_to_save = os.path.join("election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Initialize candidate options list
candidate_options = []

# Declare candidate votes dictionary
candidate_votes = {}

# Winning Candidate stat tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results file and read.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    # Read and print header row.
    headers = next(file_reader)

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


#Use with statement to open the file as a text file.
with open(file_to_save,"w") as txt_file:
    # Write election summary to election_analysis
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count into the text file.
    txt_file.write(election_results)

    # Percentage of votes for each candidate
    for candidate_name in candidate_votes:
        # Retreive vote count for each candidate
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes.
        vote_percentage = float(votes)/float(total_votes)*100
        # Print candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")
        
        print(candidate_results)
        txt_file.write(candidate_results)
    
        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true replace winning_count with votes and winning_percent with vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate to the candidate's name.
            winning_candidate = candidate_name

    # Winner of the election based on popular vote
    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

