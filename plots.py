import matplotlib.pyplot as plt
import math

names = ["trivial encoding", "bracket encoding", "improved bracket encoding", "improved bracket encoding 2"]

# Differing k:

trivial = lambda m, k: 3 * (m + k - 1)
bracket = lambda m, k: 4 * (m + (k - 1) / 3)
improved_bracket = lambda m, k: 3 * m + (4 / 3) * (k - 1)
improved_bracket2 = lambda m, k: 4 * m + k - 1

functions = [trivial, bracket, improved_bracket, improved_bracket2]


def plot_1(scaling):
    x_values = [x for x in range(1, 40)]
    for function in functions:
        y_values = []
        for x in x_values:
            y_values.append(function(m=scaling * x, k=x))
        plt.plot(x_values, y_values)
    plt.legend(names, fontsize=12)
    plt.xlabel("Anzahl Knoten")
    plt.ylabel("verbrauchter Speicherplatz")

    plt.show()

# plot_1(1)
# plot_1(5)


# Differing degree:

trivial = lambda d, m, k: 3*m + 3*(2*(k-1)/d) + 3*((k-1)/d)
bracket = lambda d, m, k: 4*m + (2*(k-1)/d) + 2*((k-1)/d)
improved_bracket = lambda d, m, k: 3*m + (2*(k-1)/d) + 2*((k-1)/d)
improved_bracket2 = lambda d, m, k: 4*m + (2*(k-1)/d) + ((k-1)/d)

functions = [trivial, bracket, improved_bracket, improved_bracket2]

x = 500
def plot_2(scaling):
    degrees = [x for x in range(2, 40)]
    for function in functions:
        y_values = []
        for d in degrees:
            y_values.append(function(d=d, m=scaling * x, k=x))
        plt.plot(degrees, y_values)
    plt.legend(names, fontsize=12)
    plt.xlabel("Verzweigungsgrad")
    plt.ylabel("verbrauchter Speicherplatz")

    plt.show()

# plot_2(1)
# plot_2(5)


# Differing amount of real language symbols

def trivial(s, d, m, k):
    n = math.ceil(math.log(s,4))
    return n*m + n*(2*(k-1)/d) + n*((k-1)/d)

def bracket(s, d, m, k):
    s -= 2
    n = math.ceil(math.log(s,3))
    return n*m + (2*(k-1)/d) + 2*((k-1)/d)

def improved_bracket(s, d, m, k):
    s -= 2
    n = math.ceil(math.log(s/3,4)) + 1
    return n*m + (2*(k-1)/d) + 2*((k-1)/d)

def improved_bracket2(s, d, m, k):
    s -= 2
    n = math.ceil(math.log(s/2,4)) + 1
    return n*m + (2*(k-1)/d) + ((k-1)/d)

functions = [trivial, bracket, improved_bracket, improved_bracket2]
# functions = [improved_bracket, improved_bracket2]
# names = ["improved bracket encoding", "improved bracket encoding 2"]

x = 500
def plot_2(scaling):
    num_sybols_to_encode = [x for x in range(5,100)]
    for function in functions:
        y_values = []
        for s in num_sybols_to_encode:
            y_values.append(function(s=s, d=3, m=scaling * x, k=x))
        plt.plot(num_sybols_to_encode, y_values)
    plt.legend(names, fontsize=12)
    plt.xlabel("Größe des Zeichensatzes")
    plt.ylabel("verbrauchter Speicherplatz")

    plt.show()

plot_2(1)
plot_2(5)

