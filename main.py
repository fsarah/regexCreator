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

        if char != '\n':
            updated_list.append(char)

        input_summary[input_len] = updated_list
        input_len += 1

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

def vagueify(input_summary):
    print (input_summary)
    for line in input_summary:
        if len(input_summary[line]) > 1:
            numbers = 0
            chars = 0
            for char in input_summary[line]:
                if char.isdigit():
                    numbers += 1
                if char.isalpha():
                    chars += 1
            if numbers > 1 and chars == 0:
                input_summary[line] = []
                input_summary[line].append("(0-9)")
            elif numbers > 1 and chars > 1:
                input_summary[line] = []
                input_summary[line].append("(0-9)|(a-z)")
            elif numbers > 1 and chars == 1:
                input_summary[line] = []
                input_summary[line].append("(0-9)")
                input_summary[line].append("char") #TODO
            elif numbers == 1 and chars > 1:
                input_summary[line] = []
                input_summary[line].append("(a-z)")
                input_summary[line].append("number") #todo
            elif numbers == 0 and chars > 0:
                input_summary[line] = []
                input_summary[line].append("(a-z)")
    return input_summary

def summarize(vague_summary):
  print(vague_summary)
  for line in vague_summary:
    if line > 0 and vague_summary[line] == vague_summary[line - 1]:
      vague_summary[line] = []
#      if vague_summary[line - 1] DOESN'T HAVE A STAR AT THE END
      #temp_string = vague_summary[line - 1]
      #temp_string = temp_string + "*"
      #vague_summary[line - 1] = temp_string
      print(vague_summary[line - 1])



def create_regex(input_summary, shortest_input_length, longest_input_length):
    regex = ""
    input_len = 0

    for line in input_summary:
        input_len += 1
        elements = input_summary[line]

        if len(elements) == 1:
            if input_len <= shortest_input_len:
                regex = regex + elements[0]
            #else if regex is already in brackets
            else:
                regex = regex + "(" + elements[0] + ")?"
        elif len(elements) > 1:
            tmp = ""

            for element in elements:
                if tmp == "":
                    tmp = tmp + element
                else:
                    tmp = tmp + "|" + element
            if input_len <= shortest_input_len:
                regex = regex + "(" + tmp + ")"
            else:
                regex = regex + "(" + tmp + ")?"
    return regex


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

baseline = len(input_summary[0])
for line in input_summary:
    if len(input_summary[line]) == baseline:
        shortest_input_len += 1
    longest_input_len += 1

#print longest_input_len
#print shortest_input_len

input_summary = simplify(input_summary)
#for line in input_summary:
#    print input_summary[line]

vague_summary = vagueify(input_summary)
summarized_summary = summarize(vague_summary)

exact_regex = create_regex(input_summary, shortest_input_len, longest_input_len)
print (exact_regex)