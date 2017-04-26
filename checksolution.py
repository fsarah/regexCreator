import re
import os

matches = []
nonmatches = []

filepath = os.path.join(os.path.dirname(__file__), 'guitars_dataset.txt')
f = open(filepath, 'r')
rex = re.compile(r"[A-Z5][A-Z4][0-9A-ZM][0-9A-ZS]?[0-9]?[0MQED1]?[A-Z]?[Z]?") # enter regex here

for line in f:
    newline = line.rstrip()

    if len(newline) > 0:
        if rex.fullmatch(newline):
            matches.append(newline)
        else:
            nonmatches.append(newline)

print("Matches =", matches)
print("NonMatches =", nonmatches)