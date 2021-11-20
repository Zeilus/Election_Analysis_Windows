# Add dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1 Initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    
    # Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #2. Add to to the total vote count.
        total_votes += 1
         # Print the candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # 2. Begin tracking taht candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) *100

        # Determine winnign vote count and candidate
        # Determine if teh vote is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent = 
            # vote_percentage = vote_percentage
            winning_count = votes
            wininng_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name
            wininng_candidate = vote_percentage
        # 4. Print the camdidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage}% of the vote")

# Print winning candidate, vote count, and percentage
# to terminal
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary =(
    f"----------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------"
)
print(winning_candidate_summary)
# # Print each row in the CSV file
    # for row in file_reader:
    #     print(row)

    # # Read the file the object with the reader function
    # file_reader = csv.reader(election_data)




# dir(csv)
# file_to_load = 'Resources/election_results.csv'


# # Open and read election results
# with open(file_to_load, 'r') as election_data:

#     # Perform Analysis
#     print(election_data)




# Write to file method 1

# Create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file
#outfile = open(file_to_save, "w")
# Write some data to the file
#outfile.write("Hello World")

# Close the file
#outfile.close()

# # Create a filename variable to a direct or indirect path to the file
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:

#     # # Write some data to the file
#     # txt_file.write("Hello World")

#     # # Write three counties to the file
#     # txt_file.write("Araphoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson")

#     # Write three counties to the file
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("-------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")







# List of candidates who received votes
# A Total number of votes each candidate received 
# Percentage of votes each candidate won
# The winner of the election based on popular vote
