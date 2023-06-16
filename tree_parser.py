# splits normal string into 3 subtree strings
def get_subtree_strings(string):
    index = 0
    substring_1, index = subtree_string(string, index)
    substring_2, index = subtree_string(string, index)
    substring_3, _ = subtree_string(string, index)

    return substring_1, substring_2, substring_3[:-1]

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
def get_subtree_strings_dna(string, bracket):
    index = 0
    substring_1, index = subtree_string_dna(string, index, bracket)
    substring_2, index = subtree_string_dna(string, index, bracket)
    substring_3, _ = subtree_string_dna(string, index, bracket)

    return substring_1, substring_2, substring_3


def subtree_string_dna(string, index, bracket):
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
            if 3 * open_brackets == num_passed_nodes: 
                break
    
    sub_string = head+sub_string
    return sub_string, index


# def parse_sub_string_dna(string, index, bracket):
#     sub_string = ""
#     open_brackets = 0
#     num_passed_nodes = 0
#     while True:
#         sequence = string[index:index+len(bracket)]
#         index += len(bracket)
#         next_sequence = string[index:index+len(bracket)]

#         if next_sequence == bracket:
#             open_brackets += 1
#         else:
#             num_passed_nodes += 1
#         sub_string += sequence
#         if 3 * open_brackets == num_passed_nodes - 1: # found full subtree
#             break
#     return sub_string, index
