import os


# Handles lines:
def handle_line(input_count, line, input_summary):
    input_len = 0

    for char in line:
        list = input_summary.get(input_len)
        updated_list = []

        if list is not None:
            for item in list:
                updated_list.append(item)

            updated_list.append(char)
        input_summary[input_len] = updated_list
        input_len += 1

    print(line)
    return input_summary

def simplify(input_summary):
    simplified_summary = {}
    for line in input_summary:
        elements = input_summary[line]
        new_list = []

        for element in elements:
            if new_list is None:
                new_list.append(element)
            else:
                found = 0
                current_list = new_list

                for list_el in current_list:
                    if element == list_el:
                        found = 1

                if found == 0 and element != '\n':
                    new_list.append(element)

        simplified_summary[line] = new_list

    return simplified_summary

def create_regex(input_summary):
    for line in input_summary:
        elements = input_summary[line]
        if len(elements) == 1:
            print "here"
        else:
            print len(elements)

# Main Function
f = open('test.txt', 'r')

input_count = 0
longest_input_len = 0
shortest_input_len = 0
input_summary = {}

for line in f:
    input_summary = handle_line(input_count, line, input_summary)
    input_count += 1

#for line in input_summary:
#    print(input_summary[line])

input_summary = simplify(input_summary)
for line in input_summary:
    print input_summary[line]

create_regex(input_summary)