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

# parse_string("node1(node2,node3,node4)")
