###################################################################################################
###################################################################################################
##  PyBank - practice with opening csv values and evaluating data
##
##  2018 08 17 - Basic implementation of opening file with comments outlining future implementation
##
###################################################################################################


################################################# Import necessary libraries
import os
import csv

################################################# Get file path for processing
filepath = input("File path/name:  ")

################################################# Open reader for main evaluation body
with open(filepath, "r",newline="") as source:

    ############################################# Set variables
    reader = csv.reader(source, delimiter=",")
    mo_ct = 0
    last_mo = ""
    last_res = 0
    balance = round(0,2)
    labels = False
    delta = []
    g_inc = ["","0"]
    g_dec = ["","0"]

    ############################################# Check for labels

    ############################################# Loop through file
    for row in reader:

        ######################################### Check for unique date

        ######################################### Evaluate change from last mo

        ######################################### Check for greatest values
    
    ############################################# Purge first delta value because of lack of history

    ############################################# Create output filename based on input filepath or user input?

    ############################################# Open writer for output of results to file

        ######################################### Write to results to file and print to terminal

###################################################################################################
###################################################################################################