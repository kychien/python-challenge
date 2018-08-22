###################################################################################################
###################################################################################################
##  PyPoll - process to modernize vote-counting process
##
##  2018 08 22 - Commented in outline of intended structure and setup output file writer.  Added in
##      voter counter.  Added in results calculation with percentages.  Added in winner check.  
##      Added in results printout.  Added in a function to help with formatting printouts.
###################################################################################################


################################################# Import necessary libraries
import os                                       #  Possibly necessary for creating output filepath?
import csv
import pandas as pdL

################################################# Get file path for processing
i_file = "election_data.csv"                    #  Initial implementation with fixed filename

################################################# Read the file into a Pandas DataFrame
csvfile = pdL.read_csv(i_file)

################################################# Count the number of unique Voter ID's
voters = csvfile["Voter ID"].unique()           
total = len(voters)

################################################# Count the number of votes for each candidate
votes = csvfile["Candidate"].value_counts()
candidates = csvfile["Candidate"].unique()


name_len = [len(name) for name in candidates]
longest = max(name_len)
################################################# Function to insert spaces to align outputs
def spacers(num_spaces):
    spaces = ""
    if (num_spaces <= 0):
        return spaces
    else:
        for i in range(num_spaces):
            spaces += " "
    return spaces


################################################# Determine winner of the election
highest = 0                                     #  Highest number of votes value
win_i = 0                                       #  Index of the winner's name in {candidates[]}
i = 0
for frame in votes:
    if (frame > highest):
        highest = frame
        win_i = i
    i += 1


################################################# Calculate the percentages of the total vote 
pct_vote = [(str("%.2f" % (line * 100 / total)) + "%") for line in votes]

################################################# Force every member of pct_vote to be 6 chars
i = 0
for frame in pct_vote:                          
    pct_vote[i] = spacers(6 - len(frame)) + frame
    i += 1



################################################# Get file path for output
o_file = "election_results.txt"                 #  Initial implementation with fixed filename

################################################# Open writer for output of results to file
with open(o_file, "w") as results:

    ############################################# Setup output data
    out_line = ["Election Results"]
    out_line.append("-------------------------")
    out_line.append(f"Total Votes: {total}")
    out_line.append("-------------------------")
    for j in range(len(candidates)):
        out_line.append(f"{spacers(longest - name_len[j])}{candidates[j]}:  {pct_vote[j]} ({votes[j]})")
    out_line.append("-------------------------")
    out_line.append(f"Winner: {candidates[win_i]}")
    out_line.append("-------------------------")
    ############################################# Print to terminal and write to file
    for line in out_line:
        print(line)
        results.write(line)
        results.write("\n")
    results.close()                             #  Close output file
    
    
###################################################################################################
###################################################################################################