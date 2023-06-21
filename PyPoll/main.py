''' PyPoll Instructions

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

'''

#import modules
import os
import csv

#path to collect data
election_data_csv = os.path.join('Resources', 'election_data.csv')

#set variable
total_votes = 0
total = 0
candidates =[]
candidate_votes = dict()
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#read the csv file
with open(election_data_csv) as csvfile:
    
    #open and read the CSV
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #loop through the data to find the total number of votes
    for row in csvreader:
    
        #count total # of voters
        total_votes += 1
        
        #candidate name
        candidate_name = row[2]
        
        #add candidates to list
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        #votes per candidate
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

print("Election Results")
print("---------------------") 
print(f"Total Votes: {int(total_votes)}")
print("---------------------")

    
    #percentage of votes each candidate won
for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        #votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) *100
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes})")
        print(candidate_results)
        
        
if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidates
        print("--------------------")
        print(f"Winner: {winning_candidate}")
        
#output results to txt
with open('analysis.txt', 'w') as f:
    
    #print results into folder
    f.write("Election Results")
    f.write("---------------------") 
    f.write(f"Total Votes: {int(total_votes)}")
    f.write("---------------------")
    f.write(candidate_results)
    f.write("---------------------")
    f.write(f"Winner: {winning_candidate}")