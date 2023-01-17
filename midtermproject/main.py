import matplotlib.pyplot as plt
import networkx as nx

def print_help():
    print("Current commands:")
    print("help: Prints this help message.")
    print("importgraph: Allows you to input a graph via an adjacency matrix.")
    print("printgraph: Prints the current graph in the form of an adjacency matrix.")
    print("")

def main():
    # print help message on first execution
    print_help()
    # sets a persistent current_graph variable
    current_graph = nx.Graph();
    while True: # infinite loop
        print("Type in command to execute, or \"help\" for a list of available commands!")
        cmd = input()
        # on one hand why does python have no switch statements
        # on the other hand in C i'd be using strncmp so this is also not that bad actually
        if(cmd == "help"):
            print_help();

if __name__ == "__main__":
    main()
