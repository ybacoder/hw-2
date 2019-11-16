"""
Yacub Bholat
Data Analysis and Visualization Boot Camp
Excel Homework
Due: 2 December 2019

Create a Python script for analyzing the financial records of your company.

Your task is to create a Python script that analyzes the records to calculate each of the following:
*The total number of months included in the dataset
*The net total amount of "Profit/Losses" over the entire period
*The average of the changes in "Profit/Losses" over the entire period
*The greatest increase in profits (date and amount) over the entire period
*The greatest decrease in losses (date and amount) over the entire period

In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""

import os
file_path = os.path.join("Resources", "budget_data.csv")

date = []
profit = []
budget = {}
with open(file_path, 'r') as file_in:
    file_in.readline()
    for line in file_in:
        line = line.split(',')
        date.append(line[0])
        profit.append(int(line[1]))

print(date)
print(profit)