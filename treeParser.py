# splits normal string into 3 subtree strings
def get_subtree_strings(string, degree):
    index = 0
    return_list = []

    for _ in range(degree):
        substring, index = subtree_string(string, index)
        if len(substring) == 0:
            break
        return_list.append(substring)
    last = return_list[-1]
    return_list[-1] = last[:-1]
    return return_list


def subtree_string(string, index):
    sub_string = ""
    open_brackets = 0
    # iterate through string from index
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


def add_closing_brackets(string, degree):
    return_string = ""
    split_string = string.split("(", 1)
    if len(split_string) == 1:
        return string
    index = 0
    comma_counter_stack = []
    for char in string:
        index += 1
        if char == "(":
            comma_counter_stack.append(0)
        if char == ",":
            comma_counter_stack[-1] = comma_counter_stack[-1] + 1
            if comma_counter_stack[-1] == degree:
                return_string += ")"
                comma_counter_stack = comma_counter_stack[:-1]
                comma_counter_stack[-1] = comma_counter_stack[-1] + 1
        return_string += char
    for _ in comma_counter_stack:
        return_string += ")"
    return return_string




