# Assignment 1: List All .txt Files and Check for a Word using glob + re.search 
# Write a script to:
# - Find all .txt files in a folder.
# - Check if any file contains the word "Python".
# - Print the file name if the word is found 
 
import glob
import re
 
files = glob.glob("Python_Assignments\\*.txt")
print(files)


for file in files:
    with open(file, 'r') as f:
        text= f.read()
        match = re.search(r"Python",text)
        if match:
            print(f"{match.group()} is found in {file}")


# Assignment 2: Match File Names Using re.match
# List all files in a folder using glob, and print only the ones that start with "data_" and end with ".csv".

import re
import glob

allFiles =glob.glob("Python_Assignments\\*")
print(allFiles)

for file in allFiles:
    # pattern = r"data_*\.csv$"  
    pattern = r".*\.txt$"  
    match = re.search(pattern,file)
    if match:
        print(f"Matched {file}")

 
# Assignment 3: Validate Phone Numbers with re.match
# Given a list of phone numbers, print only the ones that match this format:
# (123) 456-7890

import re

listOfPhoneNo = ["(123) 456-7890", "123 45 32234", "(123) 459-5677", "345555 459-5677"]
for ph in listOfPhoneNo:
    pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
    if re.match(pattern, ph):
        print("Matched phone number found:",ph)