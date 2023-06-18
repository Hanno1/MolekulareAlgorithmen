import Constants as C
from itertools import product
import string
import math


def initialize_alphabet(symbols):
    """
    initialize alphabets and save it to constants.py

    :param symbols: symbols we can use for the alphabet - list has to contain at minimum 3 elements
    """
    if len(symbols) <= 2:
        print("Length has to be greater then 2 for the bracket encoding!")
        raise ValueError

    def generator(s, l):
        # generator for unique words of given length
        arr = ["".join(i) for i in product(s, repeat=l)]
        for i in range(len(arr)):
            yield arr[i]

    def generator2(s, s_prime, l):
        # generator for unique words of given length
        arr = ["".join(i) for i in product(s, repeat=l)]
        for i in range(len(arr)):
            if arr[0] not in s_prime:
                yield arr[i]

    # chars we need in the alphabet
    all_chars = [",", "("]
    for s in string.ascii_lowercase:
        all_chars.append(s)
    for s in string.digits:
        all_chars.append(s)

    # create Logarithmic Alphabet (and inverse)
    ALPHABET_LOG = dict()
    INVERSE_ALPHABET_LOG = dict()

    length = math.ceil(math.log(len(all_chars), len(symbols)))
    g = generator(symbols, length)

    for symbol in all_chars:
        c = next(g)
        ALPHABET_LOG[symbol] = c
        INVERSE_ALPHABET_LOG[c] = symbol

    # create second alphabet - Bracket
    # "(" and "," will be handled separately and can therefore be removed
    all_chars.remove("(")
    all_chars.remove(",")

    ALPHABET_BRACKET = dict()
    INVERSE_ALPHABET_BRACKET = dict()

    ALPHABET_BRACKET[","] = symbols[0]
    ALPHABET_BRACKET["("] = symbols[0] + symbols[0]
    INVERSE_ALPHABET_BRACKET[symbols[0]] = ","
    INVERSE_ALPHABET_BRACKET[symbols[0] + symbols[0]] = "("

    length = math.ceil(math.log(len(all_chars), len(symbols) - 1))
    g = generator(symbols[1:], length)

    for symbol in all_chars:
        c = next(g)
        ALPHABET_BRACKET[symbol] = c
        INVERSE_ALPHABET_BRACKET[c] = symbol

    # create bracket improved alphabet
    ALPHABET_BRACKET_IMPROVED = dict()
    INVERSE_ALPHABET_BRACKET_IMPROVED = dict()

    ALPHABET_BRACKET_IMPROVED[","] = symbols[-1]
    ALPHABET_BRACKET_IMPROVED["("] = symbols[-1] + symbols[-1]
    INVERSE_ALPHABET_BRACKET_IMPROVED[symbols[-1]] = ","
    INVERSE_ALPHABET_BRACKET_IMPROVED[symbols[-1] + symbols[-1]] = "("

    length = 1 + math.ceil(math.log(len(all_chars) / (len(symbols) - 1), len(symbols)))
    g = generator2(symbols, symbols[:-1], length)

    for symbol in all_chars:
        c = next(g)
        ALPHABET_BRACKET_IMPROVED[symbol] = c
        INVERSE_ALPHABET_BRACKET_IMPROVED[c] = symbol

    ALPHABET_BRACKET_IMPROVED2 = dict()
    INVERSE_ALPHABET_BRACKET_IMPROVED2 = dict()

    ALPHABET_BRACKET_IMPROVED2["("] = symbols[-1]
    ALPHABET_BRACKET_IMPROVED2[","] = symbols[-2]
    INVERSE_ALPHABET_BRACKET_IMPROVED2[symbols[-1]] = "("
    INVERSE_ALPHABET_BRACKET_IMPROVED2[symbols[-2]] = ","

    length = 1 + math.ceil(math.log(len(all_chars) / (len(symbols) - 2), len(symbols)))
    g = generator2(symbols, symbols[:-2], length)

    for symbol in all_chars:
        c = next(g)
        ALPHABET_BRACKET_IMPROVED2[symbol] = c
        INVERSE_ALPHABET_BRACKET_IMPROVED2[c] = symbol

    # save alphabet to constants
    with open("Constants.py", "w") as file:
        file.write("ALPHABET_LOG = " + ALPHABET_LOG.__str__() + "\n")
        file.write("INVERSE_ALPHABET_LOG = " + INVERSE_ALPHABET_LOG.__str__() + "\n\n")

        file.write("ALPHABET_BRACKET = " + ALPHABET_BRACKET.__str__() + "\n")
        file.write("INVERSE_ALPHABET_BRACKET = " + INVERSE_ALPHABET_BRACKET.__str__() + "\n\n")

        file.write("ALPHABET_BRACKET_IMPROVED = " + ALPHABET_BRACKET_IMPROVED.__str__() + "\n")
        file.write("INVERSE_ALPHABET_BRACKET_IMPROVED = " + INVERSE_ALPHABET_BRACKET_IMPROVED.__str__() + "\n\n")

        file.write("ALPHABET_BRACKET_IMPROVED2 = " + ALPHABET_BRACKET_IMPROVED2.__str__() + "\n")
        file.write("INVERSE_ALPHABET_BRACKET_IMPROVED2 = " + INVERSE_ALPHABET_BRACKET_IMPROVED2.__str__() + "\n")

        file.close()


def get_alphabet(version):
    """
    returns the needed Alphabet

    :param version: either log, bracket or bracket_improved
    :return: Alphabet and inverse Alphabet
    """
    if version == "log":
        return C.ALPHABET_LOG, C.INVERSE_ALPHABET_LOG
    elif version == "bracket":
        return C.ALPHABET_BRACKET, C.INVERSE_ALPHABET_BRACKET
    elif version == "bracket_improved":
        return C.ALPHABET_BRACKET_IMPROVED, C.INVERSE_ALPHABET_BRACKET_IMPROVED
    print("Unknown Alphabet. Version has to be log, bracket or bracket_improved")
    raise ValueError


def translate_to_dna(word, version):
    """
    translate normal word into dna version using the alphabet

    :param word: normal word
    :param version: either log, bracket or bracket_improved, corresponding to the used algorithm
    :return: encoded string
    """
    return_string = ""
    ALP, _ = get_alphabet(version)
    for char in word:
        return_string += ALP[char]
    return return_string


def translate_from_dna(dna, version):
    """
    translate dna string to normal word using the alphabet

    :param dna: dna string
    :param version: either log, bracket or bracket_improved, corresponding to the used algorithm
    :return: decoded string
    """
    ALP, IALP = get_alphabet(version)
    return_string = ""
    # logarithmic version is simple
    if version == "log":
        length = len(ALP["a"])
        split_dna = [dna[index:index+length] for index in range(0, len(dna), length)]
    # bracket and improved bracket can be handled the same way
    elif version == "bracket" or version == "bracket_improved":
        length = len(ALP["a"])
        split_dna = []
        comma = ALP[","]
        index = 0
        while index < len(dna):
            char = dna[index]
            # search for comma, if found there might be a bracket instead, so check for it
            if char == comma:
                next_char = dna[index + 1]
                if next_char in comma:
                    split_dna.append(comma + comma)
                    index += 2
                else:
                    split_dna.append(comma)
                    index += 1
            else:
                split_dna.append(dna[index:index+length])
                index += length
    else:
        print("Unknown Version")
        raise ValueError
    # translate split to normal words using the alphabet
    try:
        for seq in split_dna:
            return_string += IALP[seq]
    except KeyError:
        print("Unknown Sequence: please check the dictionary or your input")
        raise KeyError
    return return_string
