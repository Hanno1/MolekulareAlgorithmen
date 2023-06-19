import time
from generateTree import generate_tree
from DNA_Encoder import DNA_Encoder
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from AlphabetFunctions import translate_from_dna
from treeParser import add_closing_brackets

versions = ["log", "bracket", "bracket_improved", "bracket_improved2"]
version_names = {"log":"trivial encoding", "bracket":"bracket encoding", "bracket_improved":"improved bracket encoding", "bracket_improved2":"improved bracket encoding 2"}
num_nodes_array = np.arange(0,5000,100)

def plot_time(mode="Kodieren"):
    fig = plt.figure(figsize=(12,6))
    axs = fig.subplots(1,2)
    for i, tree_type in enumerate(["b", "d"]):
        time_values = {"log": [] , "bracket": [], "bracket_improved": [], "bracket_improved2": []}
        for version in versions:
            for num_nodes in tqdm(num_nodes_array):
                breadth_tree = DNA_Encoder(version, initial_value=generate_tree(num_nodes,3,"b"))

                if mode == "Dekodieren":
                    dna = breadth_tree.tree_to_dna()
                    start_time = time.time()
                    add_closing_brackets(translate_from_dna(dna, version), 3)
                    runtime = time.time() - start_time
                if mode == "Kodieren":
                    start_time = time.time()
                    breadth_tree.tree_to_dna()
                    runtime = time.time() - start_time

                arr = time_values[version]
                arr.append(runtime)
                time_values[version] = arr

        ax = axs[i]
        type_string = "Maximale Breite" if tree_type=="b" else "Maximale Tiefe"
        ax.set_title(f"Laufzeit für {mode}, Baumtyp: {type_string}")
        ax.set_xlabel("Anzahl Knoten")
        ax.set_ylabel("Laufzeit")
        for version in versions:
            ax.plot(num_nodes_array, time_values[version], label=version_names[version])
        ax.legend()
    plt.show()

plot_time("Dekodieren")
plot_time("Kodieren")