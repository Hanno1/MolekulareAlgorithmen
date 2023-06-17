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


# splits dna string into 3 subtree strings
def get_substring_logarithmic_encoding(string, bracket, degree):
    index = 0
    return_list = []
    for _ in range(degree):
        substring, index = subtree_string_logarithmic_encoding(string, index, bracket, degree)
        if len(substring) == 0:
            break
        return_list.append(substring)
    return return_list


def subtree_string_logarithmic_encoding(string, index, bracket, degree):
    head = ""
    sub_string = ""
    open_brackets = 0
    num_passed_nodes = 0

    # iterate through string from index
    while True:
        # get next word
        sequence = string[index:index+len(bracket)]
        index += len(bracket)

        # if word is subtree head -> initialize
        if head == "": 
            head = sequence
            # break if subtree is a single node
            next_node_is_bracket = (string[index:index+len(bracket)] == bracket)
            if not next_node_is_bracket:
                break
        # else check if subtree-end is found
        else: 
            if sequence != bracket:
                num_passed_nodes += 1
            else:
                open_brackets += 1

            sub_string += sequence
            # break if subtree-end is found
            if degree * open_brackets == num_passed_nodes:
                break
    
    sub_string = head+sub_string
    return sub_string, index


def get_substring_bracket_encoding(string, bracket, length, degree):
    index = 0
    return_list = []
    for _ in range(degree):
        substring, index = subtree_string_bracket_encoding(string, index, bracket, length, degree)
        if len(substring) == 0:
            break
        return_list.append(substring)
    return return_list


def subtree_string_bracket_encoding(string, index, bracket, length, degree):
    head = ""
    sub_string = ""
    open_brackets = 0
    num_passed_nodes = 0

    # iterate through string from index
    while True:
        # get next word
        sequence = string[index:index+length]
        next_char = None
        try:
            next_char = string[index+length]
            if next_char == bracket:
                index += 1
                open_brackets += 1
        except Exception:
            pass
        
        index += length

        # if word is subtree head -> initialize
        if head == "": 
            head = sequence
            # break if subtree is a single node
            if next_char != bracket:
                break
    
        # else check if subtree-end is found
        else: 
            num_passed_nodes += 1

            sub_string += sequence
            # break if subtree-end is found
            if degree * open_brackets == num_passed_nodes:
                break
        if next_char == bracket:
            sub_string += next_char
    
    sub_string = head+sub_string
    return sub_string, index


def get_substring_suffix_encoding(string, bracket, degree):
    index = 0
    return_list = []

    for _ in range(degree):
        substring, index = _subtree_string_suffix_encoding(string, index, bracket, degree)
        if len(substring) == 0:
            break
        return_list.append(substring)
    return return_list


def _subtree_string_suffix_encoding(string, index, bracket, degree):
    head = ""
    sub_string = ""
    open_brackets = 0
    num_passed_nodes = 0

    # iterate through string from index
    if string[index] == bracket:
        index += 1
    while True:
        # get next word
        split_string = string[index:].split(bracket, 1)
        sequence = split_string[0]
        next_char = None
        try:
            next_char = split_string[1][0]
            if next_char == bracket:
                index += 1
                open_brackets += 1
        except Exception:
            pass
        
        index += len(sequence)+1

        # if word is subtree head -> initialize
        if head == "": 
            head = sequence
            # break if subtree is a single node
            if next_char != bracket:
                break
    
        # else check if subtree-end is found
        else: 
            num_passed_nodes += 1

            sub_string += sequence + bracket
            # break if subtree-end is found
            if degree * open_brackets == num_passed_nodes:
                break
        if next_char == bracket:
            sub_string += next_char
    
    sub_string = head+bracket+sub_string
    return sub_string, index


