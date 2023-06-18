import matplotlib.pyplot as plt

names = ["trivial encoding", "bracket encoding", "improved bracket encoding", "improved bracket encoding 2"]
trivial = lambda m, n: 3 * (m + n - 1)
bracket = lambda m, n: 4 * (m + (n - 1) / 3)
improved_bracket = lambda m, n: 3 * m + (4 / 3) * (n - 1)
improved_bracket2 = lambda m, n: 4 * m + n - 1

functions = [trivial, bracket, improved_bracket, improved_bracket2]


def plot_1(scaling):
    x_values = [x for x in range(1, 40)]
    for function in functions:
        y_value = []
        for x in x_values:
            y_value.append(function(m=scaling * x, n=x))
        # y_values.append(y_value)
        plt.plot(x_values, y_value)
    plt.legend(names, fontsize=12)
    plt.xlabel("Anzahl Knoten")
    plt.ylabel("verbrauchter Speicherplatz")

    # plt.plot(x_values, y_values)
    plt.show()


plot_1(5)
