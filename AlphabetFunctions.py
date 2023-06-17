import Constants as C
from itertools import product
import string
import math


def initialize_alphabet(symbols):
    if len(symbols) <= 2:
        print("Length has to be greater then 2 for the bracket encoding!")
        raise ValueError

    def generator(s, l):
        # generator for unique words of given length
        arr = ["".join(i) for i in product(s, repeat=l)]
        for i in range(len(arr)):
            yield arr[i]

    ALPHABET_LOG = dict()
    INVERSE_ALPHABET_LOG = dict()

    all_chars = [",", "("]
    for s in string.ascii_lowercase:
        all_chars.append(s)
    for s in string.digits:
        all_chars.append(s)

    length = math.ceil(math.log(len(all_chars), len(symbols)))
    g = generator(symbols, length)

    for symbol in all_chars:
        c = next(g)
        ALPHABET_LOG[symbol] = c
        INVERSE_ALPHABET_LOG[c] = symbol

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

    ALPHABET_BRACKET_IMPROVED = dict()
    INVERSE_ALPHABET_BRACKET_IMPROVED = dict()

    ALPHABET_BRACKET_IMPROVED[","] = symbols[-1]
    ALPHABET_BRACKET_IMPROVED["("] = symbols[-1] + symbols[-1]
    INVERSE_ALPHABET_BRACKET_IMPROVED[symbols[-1]] = ","
    INVERSE_ALPHABET_BRACKET_IMPROVED[symbols[-1] + symbols[-1]] = "("

    length = math.ceil(math.log(len(all_chars), len(symbols)))
    g = generator(symbols, length)

    for symbol in all_chars:
        c = next(g)
        ALPHABET_BRACKET_IMPROVED[symbol] = c
        INVERSE_ALPHABET_BRACKET_IMPROVED[c] = symbol

    with open("Constants.py", "w") as file:
        file.write("ALPHABET_LOG = " + ALPHABET_LOG.__str__() + "\n")
        file.write("INVERSE_ALPHABET_LOG = " + INVERSE_ALPHABET_LOG.__str__() + "\n\n")

        file.write("ALPHABET_BRACKET = " + ALPHABET_BRACKET.__str__() + "\n")
        file.write("INVERSE_ALPHABET_BRACKET = " + INVERSE_ALPHABET_BRACKET.__str__() + "\n\n")

        file.write("ALPHABET_BRACKET_IMPROVED = " + ALPHABET_BRACKET_IMPROVED.__str__() + "\n")
        file.write("INVERSE_ALPHABET_BRACKET_IMPROVED = " + INVERSE_ALPHABET_BRACKET_IMPROVED.__str__() + "\n")

        file.close()


def get_alphabet(version):
    if version == "log":
        return C.ALPHABET_LOG, C.INVERSE_ALPHABET_LOG
    elif version == "bracket":
        return C.ALPHABET_BRACKET, C.INVERSE_ALPHABET_BRACKET
    elif version == "bracket_improved":
        return C.ALPHABET_BRACKET_IMPROVED, C.INVERSE_ALPHABET_BRACKET_IMPROVED
    raise ValueError


def translate_to_dna(word, version):
    return_string = ""
    ALP, _ = get_alphabet(version)
    for char in word:
        return_string += ALP[char]
    return return_string


def translate_from_dna(dna, version):
    ALP, IALP = get_alphabet(version)
    return_string = ""
    if version == "log":
        length = len(ALP["a"])
        split_dna = [dna[index:index+length] for index in range(0, len(dna), length)]
    elif version == "bracket" or version == "bracket_improved":
        length = len(ALP["a"])
        split_dna = []
        comma = ALP[","]
        index = 0
        while index < len(dna):
            char = dna[index]
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
        raise ValueError
    for seq in split_dna:
        return_string += IALP[seq]
    return return_string

