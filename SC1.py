# Used: https://requests.readthedocs.io/en/latest/user/quickstart/#redirection-and-historyas reference for requests module

import requests

identifier = input("Enter the ID: ")
data = requests.get(f"https://www.southampton.ac.uk/people/{identifier}",allow_redirects=True)

def stripTags(string): # Removes HTML tags
    current = ""
    status = False
    newString = string
    for j in range(len(string)):
        if string[j] == "<" and not status:
            current += string[j]
            status = True
        elif string[j] == ">" and status:
            current += string[j]
            newString = newString.replace(current,"")
            status = False
            current = ""
        elif status:
            current += string[j]

    return newString



# Used: https://stackoverflow.com/questions/24237524/how-to-split-a-python-string-on-new-line-characters to figure out how to split lines
# Used: https://www.geeksforgeeks.org/python/check-if-string-contains-substring-in-python/ for in
datalines = data.text.splitlines() # Split the response into different lines
for i in range(len(datalines)): # Iterate over all lines in the response
    if "md:pb-2 pb-5" in datalines[i]: # Output name
        i+= 1
        line = stripTags(datalines[i]).strip()
        print(f"Name: {line}")
    elif "pb-6 text-xl" in datalines[i]: # Output Title
        line = stripTags(datalines[i]).strip()
        print(f"Title: {line}")