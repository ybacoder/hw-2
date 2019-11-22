"""
Yacub Bholat
Data Analysis and Visualization Boot Camp
Python Homework PyPoll
Due: 2 December 2019

In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
(Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentrationisn't what it used to be.)

You will be give a set of poll data called election_data.csv.
The dataset is composed of three columns: Voter ID, County, and Candidate.

Your task is to create a Python script that analyzes the votes and calculates each of the following:
*The total number of votes cast
*A complete list of candidates who received votes
*The percentage of votes each candidate won
*The total number of votes each candidate won
*The winner of the election based on popular vote.

In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""

import os
import csv
import time

in_file_path = os.path.join("Resources", "election_data.csv")

with open(in_file_path, 'r') as in_file:
    csv_reader = csv.reader(in_file)
    header = next(csv_reader)
    line = [[line[0], line[1], line[2]] for line in csv_reader]
    
    voter_id = [row[0] for row in line]
    county = [row[1] for row in line]
    candidate = [row[2] for row in line]
        
    # Solution using DictReader
    # csv_reader = csv.DictReader(in_file)
    # csv_reader = list(csv_reader)
    # line = [[int(line["Voter ID"]), line["County"], line["Candidate"]] for line in csv_reader]
    # voter_id = [row[0] for row in line]
    # county = [row[1] for row in line]
    # candidate = [row[2] for row in line]

    total_votes = len(voter_id)
    candidate_list = list(set(candidate)) # find the unique candidates
    # create a dict of candidates and their corresponding number of votes
    candidate_votes = {each_candidate : candidate.count(each_candidate) for each_candidate in candidate_list}
    # create a dict of candidates and their corresponding percent of votes
    candidate_percent_votes = {each_candidate : candidate_votes[each_candidate] / total_votes * 100 for each_candidate in candidate_list}
    
    # this block of code finds the ordered list of candidates by number of votes
    sorted_candidates = []
    candidate_votes_copy = candidate_votes.copy() # need a copy to avoid destroying the dict of candidates : votes
    for i in candidate_list: # arbitrary for loop
        # append the candidate with the most votes to a list
        sorted_candidates.append(max(candidate_votes_copy, key=candidate_votes.get))
        # pop the the candiates with the most votes from the dict
        candidate_votes_copy.pop(sorted_candidates[-1])
    winner = sorted_candidates[0]

with open("election_results.md", 'w') as out_file:
    # Output all analysis results to terminal and to out_file
    head = "Election Results"
    separator = "\n-------------------------------"
    print(head + separator)
    out_file.write(head + separator + "\n")

    total_votes_print = "Total Votes: {:,.0f}".format(total_votes)
    print(total_votes_print + separator)
    out_file.write(total_votes_print + separator + "\n")

    for each_candidate in sorted_candidates:
        sorted_candidate_print = "{}: {:.3f}% ({:,.0f} votes)".\
            format(each_candidate, candidate_percent_votes[each_candidate], candidate_votes[each_candidate])
        print(sorted_candidate_print)
        out_file.write(sorted_candidate_print + "\n")
    
    winner_print = "\nWinner: {}".format(winner)
    print(separator + winner_print + separator)
    out_file.write(separator + winner_print + separator)