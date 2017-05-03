import os
import re


# Handles lines:
def handle_line(line, input_summary):
    input_len = 0

    for char in line:
        input_list = input_summary.get(input_len)
        updated_list = []

        if input_list is not None:
            for item in input_list:
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


def string_helper(character_list):
    threshold = 3
    char_string = ""

    if len(character_list) >= threshold:
        element = character_list[0]

        if element.isdigit():
            char_string = "[0-9]"
        elif element.isupper():
            char_string = "[A-Z]"
        else:
            char_string = "[a-z]"

    elif len(character_list) > 0:
        for character in character_list:
            char_string += character

    return char_string


# if more than certain number of letters/numbers, replace with [a-z] or [0-9]
def vagueify(input_summary):

    for line in input_summary:
        if len(input_summary[line]) > 1:
            numbers = 0
            upperchars = 0
            number_array = []
            upperchar_array = []
            lowerchars = 0
            lowerchar_array = []

            for char in input_summary[line]:
                if char.isdigit():
                    numbers += 1
                    number_array.append(char)
                if char.isalpha():
                    if char.isupper():
                        upperchars += 1
                        upperchar_array.append(char)
                    else:
                        lowerchars += 1
                        lowerchar_array.append(char)

            input_summary[line] = []
            input_summary[line].append(string_helper(number_array))
            input_summary[line].append(string_helper(lowerchar_array))
            input_summary[line].append(string_helper(upperchar_array))

    return input_summary


# if multiple occurrences of same possibilities right after each other, only add one with an asterisk
def summarize(vague_summary):
    changes = False
    reg_star = re.compile(r'(.*)[*]')
    pop_these = []

    for line in vague_summary:
        if line > 0:
            val1 = vague_summary[line]
            val2 = vague_summary[line - 1]
            tempval = ""

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
            if reg_ex == str(val1).strip('[\'\']'):
                vague_summary[line] = []
                if not re.search(reg_star, str(vague_summary[line-1])):
                    temp_string = str(vague_summary[line-1]).strip('[]')
                    temp_string = temp_string.strip('\'') + "*"
                    vague_summary[line - 1] = [temp_string]
                    pop_these.append(line)
                changes = True

    decluttered_list = []
    for element in vague_summary:
        if len(vague_summary[element]) > 0:
            decluttered_list.append(vague_summary[element])

    dictionary = {}
    for i in range(0, len(decluttered_list)):
        dictionary[i] = decluttered_list[i]

    return changes, dictionary


def create_regex(input_summary, shortest_input_length):
    regex = ""
    input_len = 0

    for line in input_summary:
        input_len += 1
        elements = input_summary[line]
        reg = re.compile(r'[[].*[]]')

        if len(elements) == 1:
            if input_len < shortest_input_length:
                regex = regex + elements[0]
            elif re.search(reg, elements[0]):
                regex += elements[0] + "?"
            else:
                regex = regex + "[" + elements[0] + "]?"
        elif len(elements) > 1:
            tmp = ""

            for element in elements:
                new_el = element.strip('[]')
                tmp = tmp + new_el

            if input_len < shortest_input_length:
                regex = regex + "[" + tmp + "]"
            else:
                regex = regex + "[" + tmp + "]?"

    return regex


# Main Function
def main():
    input_file = 'tests/guitar_learn.txt'
    filepath = os.path.join(os.path.dirname(__file__), input_file)
    f = open(filepath, 'r')

    input_count = 0
    longest_input_len = 0
    shortest_input_len = 0
    input_summary = {}

    for line in f:
        input_summary = handle_line(line, input_summary)
        input_count += 1

    baseline = len(input_summary[0])
    for line in input_summary:
        if len(input_summary[line]) == baseline:
            shortest_input_len += 1
        longest_input_len += 1

    input_summary = simplify(input_summary)
    # print(input_summary)

    vague_summary = vagueify(input_summary)
    # print(vague_summary)

    summarized_summary = summarize(vague_summary)
    # print(summarized_summary)

    while summarized_summary[0]:
        summarized_summary = summarize(summarized_summary[1])
        # print(summarized_summary)

    exact_regex = create_regex(summarized_summary[1], shortest_input_len)
    print(exact_regex)

if __name__ == "__main__":
    main()
