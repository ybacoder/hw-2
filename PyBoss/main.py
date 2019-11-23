"""
Yacub Bholat
Data Analysis and Visualization Boot Camp
Python Homework PyPoll
Due: 2 December 2019

Your company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:

Import the employee_data.csv file, which currently holds employee records like the below:
-Emp ID,Name,DOB,SSN,State
-214,Sarah Simpson,1985-12-04,282-01-8166,Florida
-15,Samantha Lara,1993-09-08,848-80-7526,Colorado
-411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

Then convert and export the data to use the following format instead:
-Emp ID,First Name,Last Name,DOB,SSN,State
-214,Sarah,Simpson,12/04/1985,***-**-8166,FL
-15,Samantha,Lara,09/08/1993,***-**-7526,CO
-411,Stacy,Charles,12/20/1957,***-**-8526,PA

In summary, the required conversions are as follows:
-The Name column should be split into separate First Name and Last Name columns.
-The DOB data should be re-written into MM/DD/YYYY format.
-The SSN data should be re-written such that the first five numbers are hidden from view.
-The State data should be re-written as simple two-letter abbreviations.

Special Hint: You may find this link to be helpful—Python Dictionary for State Abbreviations.
https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
"""

import os
import csv
from us_state_abbrev import us_state_abbrev # code from afhaque

in_file_path = os.path.join("employee_data.csv")

with open(in_file_path, 'r') as in_file:
    csv_reader = csv.reader(in_file)
    header_in = next(csv_reader)
    employee_data_in = [line for line in csv_reader]
print(employee_data_in[-1][1].split(" "))

# create new header list and replace name with first/last name
header_out = header_in.copy()
header_out.insert(2, "Last Name")
header_out.insert(2, "First Name")
header_out.pop(header_in.index("Name"))
print(header_in)
print(header_out)

# create new list with the required parameters
employee_data_out = [[(employee[0])] + employee[1].split(" ") for employee in employee_data_in]
for name in employee_data_out:
    print(name)

