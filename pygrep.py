# pygrep.py - searches within a given folder and subfolders for every file containing
#             the search parameter. Prints result as filename:linenumber:linecontent
import os

searchTerm = input("Search Term: ")
print(f"Searching for {searchTerm}...")

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        with open(os.path.join(root, name), 'r') as f:
            lineNumber = 1
            while line := f.readline():
                if searchTerm in line:
                    print(f'{os.path.join(root, name)}:{lineNumber}:{line}', end='')
                lineNumber += 1