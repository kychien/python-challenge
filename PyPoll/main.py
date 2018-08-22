###################################################################################################
###################################################################################################
##  PyPoll - process to modernize vote-counting process
##
##  2018 08 22 - Commented in outline of intended structure and setup output file writer.
##      
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

################################################# Count the number of votes for each candidate

################################################# Calculate the percentages of the total vote 

################################################# Create output file
o_file = "election_results.txt"

############################################# Open writer for output of results to file
with open(o_file, "w") as results:

    ######################################### Write to results to file and print to terminal
    out_line = ["Election Results"]
    out_line.append("----------------------------")
    # Placeholder for results addition
    for line in out_line:
        print(line)
        results.write(line)
        results.write("\n")
    results.close()                    # Close output file
    
    
###################################################################################################
###################################################################################################