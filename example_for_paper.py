from DNA_Encoder import DNA_Encoder
from AlphabetFunctions import initialize_alphabet

# initialize Alphabet
# Hier kann das Alphabet verändert werden. Es muss aber mindestens 3 Zeichen geben!
initialize_alphabet(["A", "C", "T", "G"])

# Erstellung des Baums aus der Einleitung mit Encoding aus 2.1 (logarithmisch)
t1 = DNA_Encoder(version="log", initial_value="a(b(e,f(k,l,m),g),c,d(h,i,j))")
# triviale Kodierung erstellen
e1 = t1.tree_to_dna()
print(e1)
# Ergebnis: AATAACAAGAACACTAAAACGAACAGAAAAAGCAAAAGTAAAATAAAAACAAAAACCAACATCAAAATTAAAATG

# Erstellung des Baums aus dem kodierten String (gleiches Encoding!)
t2 = DNA_Encoder(version="log", dna_value=e1)
# Ausgabe des dekodierten Baums
print(t2.get_tree_string())
# Ergebnis: a(b(e,f(k,l,m),g),c,d(h,i,j))

# Erstellung des Baums aus der Einleitung mit Encoding aus 2.3.1 (verbesserter Klammeransatz)
t3 = DNA_Encoder(version="bracket_improved", initial_value="a(b(e,f(k,l,m),g),c,d(h,i,j))")
e3 = t3.tree_to_dna()
print(e3)
# Ergebnis: AAAGGAACGGACAGACCGGATTGATGGAGAGACTGAATGAAGGGACGGATAGATC

# Erstellung des Baums aus dem kodierten String (gleiches Encoding!)
t4 = DNA_Encoder(version="bracket_improved", dna_value=e3)
print(t4.get_tree_string())
# Ergebnis: a(b(e,f(k,l,m),g),c,d(h,i,j))

# Erstellung eines Baums mit Verzweigungsgrad 2 und Encoding 2.3.3
t5 = DNA_Encoder(version="bracket_improved2", branching_degree=2, initial_value="a(b,c(d(e,f),g))")
e5 = t5.tree_to_dna()
# Ergebnis: AAAAGAAACTAAATGAAAGGAACATAACCTAACT
t6 = DNA_Encoder(version="bracket_improved2", branching_degree=2, dna_value=e5)
print(t6.get_tree_string())
# Ergebnis: a(b,c(d(e,f),g))
