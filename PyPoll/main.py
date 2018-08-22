###################################################################################################
###################################################################################################
##  PyPoll - process to modernize vote-counting process
##
##  2018 08 22 - Commented in outline of intended structure and setup output file writer.  Added in
##      voter counter.  Added in results calculation with percentages.  Added in winner check.  
##      Added in results printout.
###################################################################################################


################################################# Import necessary libraries
import os                                       #  Possibly necessary for creating output filepath?
import csv
import pandas as pdL

################################################# Get file path for processing
i_file = "election_data.csv"                  # Initial implementation with fixed filename

################################################# Read the file into a Pandas DataFrame
csvfile = pdL.read_csv(i_file)

################################################# Count the number of unique Voter ID's
voters = csvfile["Voter ID"].unique()
total = len(voters)

################################################# Count the number of votes for each candidate
votes = csvfile["Candidate"].value_counts()
candidates = csvfile["Candidate"].unique()

################################################# Determine winner of the election
highest = 0
win_i = 0
i = 0
for frame in votes:
    if (frame > highest):
        highest = frame
        win_i = i
    i += 1


################################################# Calculate the percentages of the total vote 
pct_vote = [(str("%.2f" % (line * 100 / total)) + "%") for line in votes]

################################################# Create output file
o_file = "election_results.txt"

############################################# Open writer for output of results to file
with open(o_file, "w") as results:

    ######################################### Write to results to file and print to terminal
    out_line = ["Election Results"]
    out_line.append("-------------------------")
    out_line.append(f"Total Votes: {total}")
    out_line.append("-------------------------")
    for j in range(len(candidates)):
        out_line.append(f"{candidates[j]}:   {pct_vote[j]} ({votes[j]})")
    out_line.append("-------------------------")
    out_line.append(f"Winner: {candidates[win_i]}")
    out_line.append("-------------------------")
    for line in out_line:
        print(line)
        results.write(line)
        results.write("\n")
    results.close()                    # Close output file
    
    
###################################################################################################
###################################################################################################