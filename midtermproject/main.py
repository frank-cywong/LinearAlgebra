import matplotlib.pyplot as plt
import networkx as nx

# A default / sample graph in adjacency matrix form
DEFAULT_GRAPH_ADJ = [[0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1]];

# Loads default graph from an adjacently matrix
def load_default_graph():
    load_graph_from_adj_matrix(DEFAULT_GRAPH_ADJ)

# Prints help message
def print_help():
    print("Current commands:")
    print("help: Prints this help message.")
    print("importgraph: Allows you to input a graph via an adjacency matrix.")
    print("printgraph: Prints the current graph in the form of an adjacency matrix.")
    print("resetgraph: Resets the current graph to the default graph.")

# Main function
def main():
    # print help message on first execution
    print_help()
    # sets a persistent current_graph variable
    current_graph = load_default_graph()
    while True: # infinite loop
        print("Type in command to execute, or \"help\" for a list of available commands!")
        cmd = input()
        # on one hand why does python have no switch statements
        # on the other hand in C i'd be using strncmp so this is also not that bad actually
        if(cmd == "help"):
            print_help();

# Boilerplate to make Python behave more like C or Java by making it have a main function
if __name__ == "__main__":
    main()
