###################################################################################################
###################################################################################################
##  PyBank - practice with opening csv values and evaluating data
##
##  2018 08 17 - Basic implementation of opening file with comments outlining future implementation.
##      Added in handling for balance aggregation.  Added in unique month counter assuming data is
##      sorted by date. Added intake recording for delta list. Added in greatest value checkers 
##      with assumption of possible ties. Commented out currently anticipated variables
###################################################################################################


################################################# Import necessary libraries
import os                                       #  Possibly necessary for creating output filepath?
import csv

################################################# Get file path for processing
filepath = input("File path/name:  ")

################################################# Open reader for main evaluation body
with open(filepath, "r",newline="") as source:

    ############################################# Set variables:
    reader = csv.reader(source, delimiter=",")  #  csv reader for data
    mo_ct = 0                                   #  month counter for unique dates
    last_mo = ""                                #  holder for last month for comparison
    last_res = 0.0                              #  holder for last month's impact
    result = 0.0                                #  holder for this month's impact
    cur_d = 0.0                                 #  holder for delta from last month
    balance = round(0.0, 2)                     #  tracker for aggregate balance
    labels = False                              #  for label evaluation, may be unnecessary
    delta = []                                  #  tracker of delta's to calculate avg at the end
    g_inc = ["","0"]                            #  tracker for greatest increase
    g_dec = ["","0"]                            #  tracker for greatest decrease

    ############################################# Check for labels

    ############################################# Loop through file
    for line in reader:

        result = float(line[1])
        balance += round(result, 2)

        ######################################### Check for unique date
        if (last_mo != line[0]):
            mo_ct += 1
            last_mo = line[0]

        ######################################### Evaluate change from last mo
        cur_d = round((result - last_res), 2)
        delta.append(cur_d)
        last_res = result

        ######################################### Check for greatest values
        if (cur_d > float(g_inc[1])):           #  New greater increase
            g_inc = line

        elif (cur_d == float(g_inc[1])):        #  Tied greatest increase
            g_inc[0] = g_inc[0] + ", " + line[0]
        
        elif (cur_d < float(g_dec[1])):         #  New greatest decrease
            g_dec = line
        
        elif (cur_d == float(g_dec[1])):        #  Tied greatest decrease
            g_dec[0] = g_dec[0] + ", " + line[0]

    
    ############################################# Purge first delta value because of lack of history

    ############################################# Create output filename based on input filepath or user input?

    ############################################# Open writer for output of results to file

        ######################################### Write to results to file and print to terminal

###################################################################################################
###################################################################################################