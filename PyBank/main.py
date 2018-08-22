###################################################################################################
###################################################################################################
##  PyBank - practice with opening csv values and evaluating data
##
##  2018 08 22 - Fixed formating attempts to have output show 2 digits past decimal as currency.
##  2018 08 21 - Added in default file paths for opening and writing files for now.  Added in 
##      printing of results to terminal and results file. Fixed syntax errors.  Moved label check.
##      Fixed greatest value errors. Working status.
##  2018 08 17 - Basic implementation of opening file with comments outlining future implementation.
##      Added in handling for balance aggregation.  Added in unique month counter assuming data is
##      sorted by date. Added intake recording for delta list. Added in greatest value checkers 
##      with assumption of possible ties. Commented out currently anticipated variables
###################################################################################################


################################################# Import necessary libraries
import os                                       #  Possibly necessary for creating output filepath?
import csv

################################################# Get file path for processing
filepath = "budget_data.csv"
################################################# Prompt for file path or name
##if (input("Enter in a file path/name?  y/n") == y)
##    input("File path/name:  ")

################################################# Open reader for main evaluation body
with open(filepath, "r", newline="") as source:

    ############################################# Set variables:
    f_reader = csv.reader(source, delimiter=",")  #  csv reader for data
    mo_ct = 0                                   #  month counter for unique dates
    last_mo = ""                                #  holder for last month for comparison
    last_res = 0.0                              #  holder for last month's impact
    result = 0.0                                #  holder for this month's impact
    cur_d = 0.0                                 #  holder for delta from last month
    balance = 0.0                               #  tracker for aggregate balance
    first = True                                #  for label evaluation, may be unnecessary
    delta = []                                  #  tracker of delta's to calculate avg at the end
    g_inc = ["","0"]                            #  tracker for greatest increase
    g_dec = ["","0"]                            #  tracker for greatest decrease

    ############################################# Loop through file
    for line in f_reader:

        ######################################### Check for labels
        if (line[0] == "Date"):
            continue
        
        result = float(line[1])
        balance += result

        ######################################### Check for unique date
        if (last_mo != line[0]):
            mo_ct += 1
            last_mo = line[0]

        ######################################### Evaluate change from last mo
        cur_d = round((result - last_res), 2)
        delta.append(cur_d)
        last_res = result

        ######################################### Check for greatest values
        if (first):                             # Discount first delta
            first = False
            continue
        elif (cur_d > float(g_inc[1])):         #  New greater increase
            g_inc = [line[0], ("%.2f" % cur_d)]

        elif (cur_d == float(g_inc[1])):        #  Tied greatest increase
            g_inc[0] = g_inc[0] + ", " + line[0]
        
        elif (cur_d < float(g_dec[1])):         #  New greatest decrease
            g_dec = [line[0], ("%.2f" % cur_d)]
        
        elif (cur_d == float(g_dec[1])):        #  Tied greatest decrease
            g_dec[0] = g_dec[0] + ", " + line[0]

    
    ############################################# Purge first delta value because of lack of history
    delta.pop(0)
    avg_d = 0.0
    total_d = 0.0

    for d in delta:
        total_d += d
    
    avg_d = round((total_d/(mo_ct - 1)), 2)

    ############################################# Create output file
    # get input for file name
    # check if file name has / or \
        # no edits to the file path
    # else have to append ".\"?
    save_file = "budget_summary.txt"

    ############################################# Open writer for output of results to file
    with open(save_file, "w") as summary_file:

        ######################################### Write to results to file and print to terminal
        out_line = ["Financial Analysis"]
        out_line.append("----------------------------")
        out_line.append(f"Total Months: {mo_ct}")
        curr_str = "%.2f" % balance             #  Set 2 digit precision for balance
        out_line.append(f"Total: ${curr_str}")
        curr_str = "%.2f" % avg_d               #  Set 2 digit precision for average delta 
        out_line.append(f"Average Change: ${curr_str}")
        out_line.append(f"Greatest Increase in Profits: {g_inc[0]} ${g_inc[1]}")    #  Left out ()
        out_line.append(f"Greatest Decrease in Profits: {g_dec[0]} ${g_dec[1]}")    #  Left out ()
        for line in out_line:
            print(line)
            summary_file.write(line)
            summary_file.write("\n")
        summary_file.close()                    # Close output file
    
    source.close()                              # Close input file

###################################################################################################
###################################################################################################