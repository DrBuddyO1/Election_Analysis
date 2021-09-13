# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1a. The total number of votes cast.
total_votes = 0

candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
     
    # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     # Read the header row.
     headers = next(file_reader)

     # Print each row in the CSV file.
     for row in file_reader:
          total_votes += 1

          # Print the candidate name from each row.
          candidate_name = row[2]

        # If the candidate does not match any existing candidate...
          if candidate_name not in candidate_options:
          # Add it to the list of candidates.
               candidate_options.append(candidate_name)

print(total_votes)
print(candidate_options)

# 2. A complete list of the candidates that received votes. 
# 3. The percentage of votes each candidate won. 
# 4. The total number of votes each candidate won. 
# 5. The winner of the election based on popular vote. 
