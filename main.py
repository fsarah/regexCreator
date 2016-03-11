import os


# Handles lines:
def handle_line(line):
    print(line)

# Main Function
f = open('test.txt', 'r')

for line in f:
    handle_line(line)