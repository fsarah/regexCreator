import re
import os

matches = []
nonmatches = []

filepath = os.path.join(os.path.dirname(__file__), 'tests/threshold_testset.txt')
f = open(filepath, 'r')
rex = re.compile(r"[ACD][134][245][356][467]") # enter regex here

for line in f:
    newline = line.rstrip()

    if len(newline) > 0:
        if rex.fullmatch(newline):
            matches.append(newline)
        else:
            nonmatches.append(newline)

print("Matches =", matches)
print("NonMatches =", nonmatches)