import re

def handle_line(line, input_summary):
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


def main():
    f = open('test.txt', 'r')
    input_summary = {}
    regex = {}

    for line in f:
        input_summary = handle_line(line, input_summary)

    for position in input_summary:
        temp = input_summary[position][0]
        same = True
        for character in input_summary[position]:
            if character is not temp:
                same = False
            print(same)
        if (same):
            regex[position] = temp

    print(regex)
    match = False

    while not match:
        print("NO")
        match = True

if __name__ == "__main__":
    main()