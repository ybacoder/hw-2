"""
Yacub Bholat
Data Analysis and Visualization Boot Camp
Python Homework PyBank
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
import csv

in_file_path = os.path.join("Resources", "budget_data.csv")

# date = [] # commented out because no longer needed for more efficient solution
# profit = []
with open(in_file_path, 'r') as in_file:
    # This was my previous, less efficient solution.
    # header = in_file.readline()
    # for line in in_file:
    #     line = line.split(',')
    #     date.append(line[0])
    #     profit.append(int(line[1]))
    csv_reader = csv.DictReader(in_file)
    data = list(csv_reader)
    # extract the date and profit data into separate lists
    date = [date["Date"] for date in data]
    profit = [int(p["Profit/Losses"]) for p in data]

total_months = len(date)
total_profit = sum(profit)

# zip together the profit list offset by one index (exclude first value) with the profit list (exclude last value), then calculate profit difference for each index
profit_df = [profit_current - profit_prev for profit_current, profit_prev in zip(profit[1:], profit[:-1])]
average_profit_df = sum(profit_df) / len(profit_df)

max_profit_df = max(profit_df)
max_profit_df_index = profit_df.index(max_profit_df)
max_profit_date = date[max_profit_df_index + 1]
min_profit_df = min(profit_df)
min_profit_df_index = profit_df.index(min_profit_df)
min_profit_date = date[min_profit_df_index + 1]

with open("financial_analysis_output.md", 'w') as out_file:
    # Output all analysis results to terminal and to out_file
    head = "Financial Analysis\n-------------------------------" 
    print(head)
    out_file.write(head + "\n")

    total_months_print = "Total Months: " + str(total_months)
    print(total_months_print)
    out_file.write(total_months_print + "\n")

    total_profit_print = "Total: ${:,.0f}".format(total_profit)
    print(total_profit_print)
    out_file.write(total_profit_print + "\n")

    average_profit_df_print = "Average Change: ${:,.2f}".format(average_profit_df)
    print(average_profit_df_print)
    out_file.write(average_profit_df_print + "\n")

    greatest_profit_increase_print = "Greatest Increase in Profits: {} ${:,.0f}".format(max_profit_date, max_profit_df)
    print(greatest_profit_increase_print)
    out_file.write(greatest_profit_increase_print + "\n")

    greatest_profit_decrease_print = "Greatest Decrease in Profits: {} ${:,.0f}".format(min_profit_date, min_profit_df)
    print(greatest_profit_decrease_print)
    out_file.write(greatest_profit_decrease_print)