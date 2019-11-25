"""
Yacub Bholat
Data Analysis and Visualization Boot Camp
Python Homework PyPararaph
Due: 2 December 2019

In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:
*Import a text file filled with a paragraph of your choosing.
*Assess the passage for each of the following:
    Approximate word count
    Approximate sentence count
    Approximate letter count (per word)
    Average sentence length (in words)
*As an example, this passage:
    “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword
    point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the
    King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung
    together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the
    world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his
    detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of
    crimson and gold.”

...would yield these results:

Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.6
Average Sentence Length: 24.0

Special Hint: You may find this code snippet helpful when determining sentence length (look into regular expressions if interested in learning more):
https://en.wikipedia.org/wiki/Regular_expression
import re
re.split("(?<=[.!?]) +", paragraph)
"""

import os
import re
import csv

paragraph1_path = os.path.join("raw_data", "paragraph_1.txt")
paragraph2_path = os.path.join("raw_data", "paragraph_2.txt")
paragraph3_path = os.path.join("raw_data", "paragraph_3.txt")

# import the paragraph into a variable
# with open(paragraph1_path, 'r') as in_file:
# with open(paragraph2_path, 'r') as in_file:
with open(paragraph3_path, 'r') as in_file:
    paragraph = in_file.read()
print(paragraph + "\n")

# split the paragraph into sentences using the code from the prompt
sentences = re.split("(?<=[.!?]) +", paragraph)
print(sentences)
print("\n")

# split the sentences into words after removing all punctuation
words = "".join([char for char in paragraph if char not in ["\"", "\'", "(", "?", "<", "=", "[", ".", "!", "?", "]", ")", "+", ",", "\\"]])
words_list = words.split(" ")
print(len(words_list))

with open("paragraph_analysis.md", 'w') as out_file:
    # Output all analysis results to terminal and to out_file
    head = "Paragraph Analysis"
    separator = "\n-------------------------------"
    print(head + separator)
    out_file.write(head + separator + "\n")
