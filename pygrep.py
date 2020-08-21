# pygrep.py - searches within a given folder and subfolders for every file containing
#             the search parameter. Prints result as filename:linenumber:linecontent
import os

while __name__ == "__main__":
    searchString = input("Search String: ")
    fileType     = input("Extension: ")
    print(f"Searching for {searchString} of filetype {fileType}...")

    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if fileType == '*' or name.endswith(fileType):
                try:
                    with open(os.path.join(root, name), 'r') as f:
                        lineNumber = 1
                        while line := f.readline():
                            if searchString in line:
                                print(f'{os.path.join(root, name)}:{lineNumber}:{line}', end='')
                            lineNumber += 1
                except:
                    print(f'Error at file: {os.path.join(root, name)}')
                    continue