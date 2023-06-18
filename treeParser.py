def get_subtree_strings(string, degree):
    """
    gets a string and splits it into substrings depending of the graph degree. Will be 3 normally.
    For Example the input might be "a(b,c,d),e,f(1,2,3)" the the function will split this into
    "a(b,c,d)", "e" and "f(1,2,3)"

    :param string: input string to split - first char will not be a bracket
    :param degree: degree of the tree. 3
    :return: list of substrings
    """
    # splits normal string into 3 subtree strings
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
    """
    gets string and searches for closing bracket on the same level

    :param string: substring to handle
    :param index: index from there to start the search
    :return: substring there a bracket opens and a bracket closes on the same level.
             index there we are in the main string
    """
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
    """
    gets string without closing brackets and adds the brackets. Computes the position of the brackets
    by counting commas on levels using a stack (comma_counter_stack)

    :param string: string without closing brackets
    :param degree: degree of the tree
    :return: string with closing brackets
    """
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
