import os
import re

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

        if len(updated_list) > 0:
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

#if more than certain number of letters/numbers, replace with [a-z] or [0-9]
def vagueify(input_summary):
#    print (input_summary)
    for line in input_summary:
        if len(input_summary[line]) > 1:
            numbers = 0
            chars = 0
            number_array = []
            char_array = []
            for char in input_summary[line]:
                if char.isdigit():
                    numbers += 1
                    number_array.append(char)
                if char.isalpha():
                    chars += 1
                    char_array.append(char)
            if numbers > 1 and chars == 0:
                input_summary[line] = []
                input_summary[line].append("(0-9)")
            elif numbers > 1 and chars > 1:
                input_summary[line] = []
                input_summary[line].append("(0-9)|(a-z)")
            elif numbers > 1 and chars == 1:
                input_summary[line] = []
                input_summary[line].append("(0-9)")
                input_summary[line].append(char_array.pop(0))
            elif numbers == 1 and chars > 1:
                input_summary[line] = []
                input_summary[line].append("(a-z)")
                input_summary[line].append(number_array.pop(0))
            elif numbers == 0 and chars > 0:
                input_summary[line] = []
                input_summary[line].append("(a-z)")
    return input_summary

# if multiple occurences of same possibilities right after each other, only add one with an asterisk
def summarize(vague_summary):
#  print("vague_summary: ", vague_summary)
  reg_star = re.compile(r'(.*)[*]')

  for line in vague_summary:
    if line > 0:
      val1 = vague_summary[line]
      val2 = vague_summary[line - 1]
      tempval = ""

#      print("val1: ", val1)
#      print("val2: ", val2)
      if re.match(r"[(]", str(val1)):
        for i in 1, (len(val1) - 1):
          tempval += val1[i]
        val1 = tempval

      tempval = ""
      if re.match(r"[(]", str(val2)):
        for i in 1, (len(val1) - 1):
          tempval += val1[i]
        val1 = tempval

      if len(val2) > len(val1):
        temp = val1
        val1 = val2
        val2 = temp

      reg_ex = str(val2).strip('[\'\']')
#      reg = re.compile(r'{}'.format(reg_ex))
      if reg_ex == str(val1).strip('[\'\']'):
      #if re.match(reg, str(val1).strip('[\'\']')):
        #print("val1 & val2 match")
        vague_summary[line] = []
        if not re.search(reg_star, str(vague_summary[line-1])):
          temp_string = str(vague_summary[line-1]).strip('[]')
          temp_string = temp_string.strip('\'') + "*"
          vague_summary[line - 1] = [temp_string]

  decluttered_list = {}
  for element in vague_summary:
    if len(vague_summary[element]) > 0:
        decluttered_list[element] = vague_summary[element]

  return decluttered_list

def create_regex(input_summary, shortest_input_length, longest_input_length):
#    print("create_regex: ", input_summary)
    regex = ""
    input_len = 0

    for line in input_summary:
        input_len += 1
        elements = input_summary[line]
        reg = re.compile(r'[(].*[)]')

        if len(elements) == 1:
            if input_len <= shortest_input_length:
                regex = regex + elements[0]
            elif re.search(reg, elements[0]):
                regex += elements[0] + "?"
            else:
                regex = regex + "(" + elements[0] + ")?"
        elif len(elements) > 1:
            tmp = ""

            for element in elements:
                if tmp == "":
                    tmp = tmp + element
                else:
                    tmp = tmp + "|" + element
            if input_len <= shortest_input_length:
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

baseline = len(input_summary[0])
for line in input_summary:
    if len(input_summary[line]) == baseline:
        shortest_input_len += 1
    longest_input_len += 1

input_summary = simplify(input_summary)

vague_summary = vagueify(input_summary)

summarized_summary = summarize(vague_summary)

exact_regex = create_regex(summarized_summary, shortest_input_len, longest_input_len)
print(exact_regex)