# Import data from csv file
import csv
import os
dir(csv)
file_to_load = 'Resources/election_results.csv'


# Open and read election results
with open(file_to_load, 'r') as election_data:

    # Perform Analysis
    print(election_data)




# Write to file method 1

# Create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file
#outfile = open(file_to_save, "w")
# Write some data to the file
#outfile.write("Hello World")

# Close the file
#outfile.close()

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    # # Write some data to the file
    # txt_file.write("Hello World")

    # # Write three counties to the file
    # txt_file.write("Araphoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")

    # Write three counties to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")





# List of candidates who received votes
# A Total number of votes each candidate received 
# Percentage of votes each candidate won
# The winner of the election based on popular vote
