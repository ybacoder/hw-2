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

in_file_path = os.path.join("Resources", "election_data.csv")

with open(in_file_path, 'r') as in_file:
    csv_reader = csv.DictReader(in_file)
    csv_reader = list(csv_reader)
    print(csv_reader)
    # voter_id, county, candidate = [(int(line["Voter ID"]), line["County"], line["Candidate"]) for line in csv_reader]
    # county = [line["County"] for line in csv_reader]
    # candidate = [line["Candidate"] for line in csv_reader]
    # print(voter_id[0])