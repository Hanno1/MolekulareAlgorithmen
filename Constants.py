from itertools import product
import string
import math



BASE_SYMBOLS = ["C", "T", "G", "A"]

ALPHABET_LOG = {'(': 'AAA', ',': 'AAC', 'a': 'AAT', 'b': 'AAG', 'c': 'ACA', 'd': 'ACC', 'e': 'ACT', 'f': 'ACG', 'g': 'ATA', 'h': 'ATC', 'i': 'ATT', 'j': 'ATG', 'k': 'AGA', 'l': 'AGC', 'm': 'AGT', 'n': 'AGG', 'o': 'CAA', 'p': 'CAC', 'q': 'CAT', 'r': 'CAG', 's': 'CCA', 't': 'CCC', 'u': 'CCT', 'v': 'CCG', 'w': 'CTA', 'x': 'CTC', 'y': 'CTT', 'z': 'CTG', '0': 'CGA', '1': 'CGC', '2': 'CGT', '3': 
'CGG', '4': 'TAA', '5': 'TAC', '6': 'TAT', '7': 'TAG', '8': 'TCA', '9': 'TCC'}
INVERSE_ALPHABET_LOG = {'AAA': '(', 'AAC': ',', 'AAT': 'a', 'AAG': 'b', 'ACA': 'c', 'ACC': 'd', 'ACT': 'e', 'ACG': 'f', 'ATA': 'g', 'ATC': 'h', 'ATT': 'i', 'ATG': 'j', 'AGA': 'k', 'AGC': 'l', 'AGT': 'm', 'AGG': 'n', 'CAA': 'o', 'CAC': 'p', 'CAT': 'q', 'CAG': 'r', 'CCA': 's', 'CCC': 't', 'CCT': 'u', 'CCG': 'v', 'CTA': 'w', 'CTC': 'x', 'CTT': 'y', 'CTG': 'z', 'CGA': '0', 'CGC': '1', 'CGT': '2', 'CGG': '3', 'TAA': '4', 'TAC': '5', 'TAT': '6', 'TAG': '7', 'TCA': '8', 'TCC': '9'}

ALPHABET_BRACKET = {'(': 'AA', ',': 'A', 'a': 'CCCC', 'b': 'CCCT', 'c': 'CCCG', 'd': 'CCTC', 'e': 'CCTT', 'f': 'CCTG', 'g': 'CCGC', 'h': 'CCGT', 'i': 'CCGG', 'j': 'CTCC', 'k': 'CTCT', 'l': 'CTCG', 'm': 'CTTC', 'n': 'CTTT', 'o': 'CTTG', 'p': 'CTGC', 'q': 'CTGT', 'r': 'CTGG', 's': 'CGCC', 't': 'CGCT', 'u': 'CGCG', 'v': 'CGTC', 'w': 'CGTT', 'x': 'CGTG', 'y': 'CGGC', 'z': 'CGGT', '0': 'CGGG', '1': 
'TCCC', '2': 'TCCT', '3': 'TCCG', '4': 'TCTC', '5': 'TCTT', '6': 'TCTG', '7': 'TCGC', '8': 'TCGT', '9': 'TCGG'}
INVERSE_ALPHABET_BRACKET = {'AA': '(', 'A': ',', 'CCCC': 'a', 'CCCT': 'b', 'CCCG': 'c', 'CCTC': 'd', 'CCTT': 'e', 'CCTG': 'f', 'CCGC': 'g', 'CCGT': 'h', 'CCGG': 'i', 'CTCC': 'j', 'CTCT': 'k', 'CTCG': 'l', 'CTTC': 'm', 'CTTT': 'n', 'CTTG': 'o', 'CTGC': 'p', 'CTGT': 'q', 'CTGG': 'r', 'CGCC': 's', 'CGCT': 't', 'CGCG': 'u', 'CGTC': 'v', 'CGTT': 'w', 'CGTG': 'x', 'CGGC': 'y', 'CGGT': 'z', 'CGGG': '0', 'TCCC': '1', 'TCCT': '2', 'TCCG': '3', 'TCTC': '4', 'TCTT': '5', 'TCTG': '6', 'TCGC': '7', 'TCGT': '8', 'TCGG': '9'}

ALPHABET_BRACKET_IMPROVED = {',': 'A', '(': 'AA', 'a': 'CCC', 'b': 'CCT', 'c': 'CCG', 'd': 'CCA', 'e': 'CTC', 'f': 'CTT', 'g': 'CTG', 'h': 'CTA', 'i': 'CGC', 'j': 'CGT', 'k': 'CGG', 'l': 'CGA', 'm': 'CAC', 'n': 
'CAT', 'o': 'CAG', 'p': 'CAA', 'q': 'TCC', 'r': 'TCT', 's': 'TCG', 't': 'TCA', 'u': 'TTC', 'v': 'TTT', 'w': 'TTG', 'x': 'TTA', 'y': 'TGC', 'z': 'TGT', '0': 'TGG', '1': 'TGA', '2': 'TAC', '3': 'TAT', '4': 'TAG', '5': 'TAA', '6': 'GCC', '7': 'GCT', '8': 'GCG', '9': 'GCA'}
INVERSE_ALPHABET_BRACKET_IMPROVED = {'A': ',', 'AA': '(', 'CCC': 'a', 'CCT': 'b', 'CCG': 'c', 'CCA': 'd', 'CTC': 'e', 'CTT': 'f', 'CTG': 'g', 'CTA': 'h', 'CGC': 'i', 'CGT': 'j', 'CGG': 'k', 'CGA': 'l', 'CAC': 'm', 'CAT': 'n', 'CAG': 'o', 'CAA': 'p', 'TCC': 'q', 'TCT': 'r', 'TCG': 's', 'TCA': 't', 'TTC': 'u', 'TTT': 'v', 'TTG': 'w', 'TTA': 'x', 'TGC': 'y', 'TGT': 'z', 'TGG': '0', 'TGA': '1', 'TAC': '2', 'TAT': '3', 'TAG': '4', 'TAA': '5', 'GCC': '6', 'GCT': '7', 'GCG': '8', 'GCA': '9'}

def get_alphabet(version):
    ALP = None
    if version == "log":
        return ALPHABET_LOG, INVERSE_ALPHABET_LOG
    elif version == "bracket":
        return ALPHABET_BRACKET, INVERSE_ALPHABET_BRACKET
    elif version == "bracket_improved":
        return ALPHABET_BRACKET_IMPROVED, INVERSE_ALPHABET_BRACKET_IMPROVED
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
    for seq in split_dna:
        return_string += IALP[seq]
    return return_string


# print(translate_from_dna(translate_to_dna("hel(lo(wor,l,d", version = "bracket_improved"), version = "bracket_improved"))


# def generator(length, symbols):

#     # generator for unique words of given length
#     arr = ["".join(i) for i in product(symbols, repeat=length)]
#     for i in range(len(arr)):
#         yield arr[i]


# ALPHABET_BRACKET_IMPROVED[","] = "A"
# ALPHABET_BRACKET_IMPROVED["("] = "AA"
# INVERSE_ALPHABET_BRACKET_IMPROVED["A"] = ","
# INVERSE_ALPHABET_BRACKET_IMPROVED["AA"] = "("

# symbols = []
# for s in string.ascii_lowercase:
#     symbols.append(s)
# for s in string.digits:
#     symbols.append(s)

# length = math.ceil(math.log(len(symbols), len(BASE_SYMBOLS)))
# g = generator(length, BASE_SYMBOLS)

# for symbol in symbols:
#     c = next(g)
#     ALPHABET_BRACKET_IMPROVED[symbol] = c
#     INVERSE_ALPHABET_BRACKET_IMPROVED[c] = symbol
    

# print(ALPHABET_BRACKET_IMPROVED)
# print(INVERSE_ALPHABET_BRACKET_IMPROVED)
