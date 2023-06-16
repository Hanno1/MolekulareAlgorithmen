def parse_string(string):
    index = 0
    substring_1, index = parse_sub_string(string, index)
    substring_2, index = parse_sub_string(string, index)
    substring_3, _ = parse_sub_string(string, index)

    return substring_1, substring_2, substring_3[:-1]


def parse_sub_string(string, index):
    sub_string = ""
    open_brackets = 0
    for char in string[index:]:
        index += 1
        if char == "(":
            open_brackets += 1
        elif char == ")":
            open_brackets -= 1
        if char == "," and open_brackets == 0:
            break
        sub_string += char
    return sub_string, index

def parse_string2(string, bracket):
    index = 0
    substring_1, index = parse_sub_string2(string, index, bracket)
    substring_2, index = parse_sub_string2(string, index, bracket)
    substring_3, _ = parse_sub_string2(string, index, bracket)

    return substring_1, substring_2, substring_3


def parse_sub_string2(string, index, bracket):
    sub_string = ""
    open_brackets = 0
    c = 0
    while True:
        sequence = string[index:index+len(bracket)]
        index += len(bracket)
        next_sequence = string[index:index+len(bracket)]
        if next_sequence == bracket:
            open_brackets += 1
        else:
            c += 1
        sub_string += sequence
        if 3 * open_brackets == c - 1:
            break
    return sub_string, index
