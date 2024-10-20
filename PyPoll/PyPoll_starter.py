# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os
# identify current working directory
print("Current working directory:", os.getcwd())
# Files to load and output (update with correct file paths)
input_file = os.path.join( "Resources", "election_data.csv")  # Input file path
output_file = os.path.join("analysis", "election_analysis.txt")  # Output file path

    # initializing variables for total_votes and candidates
total_votes = 0
candidates = {}
    
    # Read the CSV file
with open(input_file,'r') as file:
    csvreader = csv.DictReader(file)
    # Skip the header row
    header = next(csvreader)
    #print(header)    
        # Iterate over each row in the CSV file
    for row in csvreader:
        total_votes= total_votes+ 1
        candidate = row['Candidate']
            
            # If the candidate is already in the dictionary, increment their vote count
        if candidate in candidates:
            candidates[candidate]= candidates[candidate]+ 1
        else:
            candidates[candidate] = 1

    # Print the calculate results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    # initializing variables for winner
    winner = None
    max_votes = 0
    
    # Calculate percentage of votes and print each candidate's results
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes} votes)")        
        # Determine the winner
        if votes > max_votes:
            max_votes = votes
            winner = candidate
     # print the blank lines(separator) and winner
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    # Open the output folder to write the results in text file(election_analysis.txt)
    with open(output_file,'w') as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")   
        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            file.write(f"{candidate}: {percentage:.3f}% ({votes} votes)\n")  
        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")



