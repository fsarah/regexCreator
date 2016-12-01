import re

matches = []
nonmatches = []

f = open('test_long.txt', 'r')
rex = re.compile(r"(0-9)((0-9)|(a-z))*(0-9)*") # enter regex here

for line in f:
    newline = line.rstrip()
    if rex.match(newline):
        matches.append(newline)
    else:
        nonmatches.append(newline)

print("Matches: ", matches)
print("NonMatches: ", nonmatches)