import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Create a list for the counties
counties = []
# Create a dictionary with county as key and votes cast for each county are values
county_votes = {}
# largest_county_turnout tracker
largest_county_turnout = ""
largest_county_count = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    
    
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Read the county name from each row.
        county_name = row[1]
        # Add County name to county list
        if county_name not in counties:
            counties.append(county_name)
            # Begin counting that county's vote count
            county_votes[county_name] = 0
        # Add a vote to that county's count
        county_votes[county_name] += 1
            
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n\n"
        f"County Votes:\n")

    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Determine the percentage of votes for each candiate and county.
    # Iterate through the county and candidate list.
    for county in county_votes:
        # Retrieve vote count of counties
        votes_by_county = county_votes[county]
        # Calculate percentage of votes
        county_vote_percentage = float(votes_by_county) / float(total_votes) * 100
        # Print county, vote count, and percentage to the terminal
        county_results = (f"{county}: {county_vote_percentage:.1f}% ({votes_by_county:,})\n")
        print(county_results)
        # Save county results to text file.
        txt_file.write(county_results)

   # Determine county with the greatest turnout
        #Determine if the votes is greater than the largest county count.
        if (votes_by_county > largest_county_count):
            # If true then set largest county count = votes by county
            largest_county_count = votes_by_county
            # And, set the largest county turnout equal to the county
            largest_county_turnout = county
    # Print largest county turnout and write to text file
    largest_county_turnout_summary = (
        f"\n--------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"--------------------------\n")
    print(largest_county_turnout_summary)
    txt_file.write(largest_county_turnout_summary)

    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    
        # To do: print out each candidate's name, vote count, and percentage of 
        # votes to the terminal

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        #Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning count = votes and winning percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate
    # Print winning candidate summary and write to text file
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    


