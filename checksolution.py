import re

matches = []
nonmatches = []

f = open('test_long.txt', 'r')
rex = re.compile(r"[0-9][0-9A-Z]*[0-9]*[0-9]?[2]?[a]?") # enter regex here

for line in f:
    newline = line.rstrip()

    if len(newline) > 0:
        if rex.fullmatch(newline):
            matches.append(newline)
        else:
            nonmatches.append(newline)

print("Matches =", matches)
print("NonMatches =", nonmatches)