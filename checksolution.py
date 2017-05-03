import re
import os

matches = []
nonmatches = []

filepath = os.path.dirname(__file__) + '/tests/guitars_test.txt'
#filepath = os.path.join(os.path.dirname(__file__), '\tests\guitars_test.txt')
f = open(filepath, 'r')
rex = re.compile(r"[5A-Z][4A-Z][0-9M][0-9S]?[0-9]?[0-9A-Z]?[A-Z]?[Z]?") # enter regex here

for line in f:
    newline = line.rstrip()

    if len(newline) > 0:
        if rex.fullmatch(newline):
            matches.append(newline)
        else:
            nonmatches.append(newline)

file = open(os.path.dirname(__file__) + '/tests/guitars_results.txt', 'w')
file.write("matches: " + str(matches) + "\n")
file.write("nonmatches: " + str(nonmatches))
file.close()

print("Matches =", matches)
print("NonMatches =", nonmatches)