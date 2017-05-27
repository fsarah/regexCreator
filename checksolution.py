import os
import re

matches = []
nonmatches = []

filepath = os.path.dirname(__file__) + '/tests/guitars_test.txt'
f = open(filepath, 'r')

#res_f = open(os.path.dirname(__file__) + '/guitars_test_threshold_results_shouldbe.txt', 'r')
file = open(os.path.dirname(__file__) + '/tests/guitars_results.txt', 'w')
#i = 1

#for rline in res_f.readlines():
#    rex = re.compile(rline.rstrip().strip('')) # enter regex here
#    file.write(str(rex) + '\n')

#    for line in f:
#        newline = line.rstrip()

#        if len(newline) > 0:
#            if rex.fullmatch(newline):
#                matches.append(newline)
#            else:
#                nonmatches.append(newline)

#    file.write("threshold = " + str(i) + "\n")
#    file.write("matches: " + str(matches) + "\n")
#    file.write("nonmatches: " + str(nonmatches) + "\n\n")

#    i += 1

rex = re.compile(r'[5RJSM][4GPZET][357801M][215703S]?[1072]?[017MQED]?[HMXZ]?[Z]?') # enter regex here
file.write(str(rex) + '\n')

for line in f:
    newline = line.rstrip()

    if len(newline) > 0:
        if rex.fullmatch(newline):
            matches.append(newline)
        else:
            nonmatches.append(newline)

#file.write("threshold = " + str(i) + "\n")
#file.write("matches: " + str(matches) + "\n")
#file.write("nonmatches: " + str(nonmatches) + "\n\n")

print("matches: " + str(matches))
print("nonmatches: " + str(nonmatches) + "\n\n")


file.close()
