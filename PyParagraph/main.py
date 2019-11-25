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

paragraph_num = "2"
paragraph_path = os.path.join("raw_data", "paragraph_" + paragraph_num + ".txt")


# import the paragraph into a variable
with open(paragraph_path, 'r') as in_file:
    paragraph = in_file.read()

# split the paragraph into sentences using the code from the prompt
sentences = re.split("(?<=[.!?]) +", paragraph)
approx_sentences_count = len(sentences)

# split the sentences into words after removing all punctuation
words = "".join([char for char in paragraph if char not in ["\"", "\'", "(", "?", "<", "=", "[", ".", "!", "?", "]", ")", "+", ",", "\\"]])
words_list = words.split(" ")
approx_words_count = len(words_list)

# split the words into characters and calculate average letter count
characters_only = words.replace(" ", "")
characters_count = len(characters_only)
avg_letter_count = characters_count / approx_words_count

# calculate average sentence length (i.e., words per sentence)
avg_sentence_length = approx_words_count / approx_sentences_count

with open("paragraph_" + paragraph_num + "_analysis.md", 'w') as out_file:
    # Output all analysis results to terminal and to out_file
    head = "Paragraph Analysis"
    separator = "\n-------------------------------"
    print(head + separator)
    out_file.write(head + separator + "\n")

    approx_words_count_print = f"Approximate Word Count: {approx_words_count}"
    print(approx_words_count_print)
    out_file.write(approx_words_count_print + "\n")

    approx_sentences_count_print = f"Approximate Sentence Count: {approx_sentences_count}"
    print(approx_sentences_count_print)
    out_file.write(approx_sentences_count_print + "\n")    
    
    avg_letter_count_print = f"Average Letter Count (i.e., letters per word): {avg_letter_count:.2f}"
    print(avg_letter_count_print)
    out_file.write(avg_letter_count_print + "\n")
    
    avg_sentence_length_print = f"Average Sentence Length (i.e., words per sentence): {avg_sentence_length:.1f}"
    print(avg_sentence_length_print)
    out_file.write(avg_sentence_length_print + "\n")