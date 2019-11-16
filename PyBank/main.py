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
with open(file_path, 'r') as file_in:
    file_in.readline()
    for line in file_in:
        line = line.split(',')
        date.append(line[0])
        profit.append(int(line[1]))

total_months = len(date)
print(total_months)

total_profit = sum(profit)
print(total_profit)

profit_df_date = date[1:]
profit_df = [profit_current - profit_prev for profit_current, profit_prev in zip(profit[1:], profit[:-1])]
average_profit_df = sum(profit_df) / len(profit_df)
print(average_profit_df)

max_profit_df = max(profit_df)
max_profit_df_index = profit_df.index(max_profit_df)
max_profit_date = date[max_profit_df_index + 1]
print(max_profit_date, max_profit_df)

min_profit_df = min(profit_df)
min_profit_df_index = profit_df.index(min_profit_df)
min_profit_date = date[min_profit_df_index + 1]
print(min_profit_date, min_profit_df)