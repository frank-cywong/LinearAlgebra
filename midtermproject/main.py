import matplotlib.pyplot as plt
import networkx as nx

# A default / sample graph in adjacency matrix form
# A[i, j] is 1 if there is an edge connecting i to j
DEFAULT_GRAPH_ADJ = [[0, 1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0]];

# Checks if matrix is square
def is_square(matrix):
    row_count = len(matrix)
    for row in matrix:
        # len(row) is col count in that row
        if(len(row) != row_count):
            return False
    return True

# Loads a graph from an adjacency matrix
def load_graph_from_adj_matrix(adj_matrix):
    # Check if square matrix
    if(not is_square(adj_matrix)):
        raise Exception("Adjacency matrix is not square!")
    # Creates directed graph object
    output_graph = nx.DiGraph();
    # Initializes nodes of matrix
    output_graph.add_nodes_from(range(len(adj_matrix)));
    # Actually draw edges
    for start_node in range(len(adj_matrix)):
        cur_row = adj_matrix[start_node]
        for end_node in range(len(cur_row)):
            if(cur_row[end_node] == 1):
                output_graph.add_edge(start_node, end_node)
    return output_graph


# Loads default graph from an adjacently matrix
def load_default_graph():
    return load_graph_from_adj_matrix(DEFAULT_GRAPH_ADJ)

# Prints help message
def print_help():
    print("Current commands:")
    print("exit: Terminates this program.")
    print("help: Prints this help message.")
    print("importgraph: Allows you to input a graph via a adjacency matrix.")
    #print("printgraph: Prints the current graph in the form of an adjacency matrix.") - not needed, use showgraph instead
    print("showgraph: Displays the current graph with Matplotlib.")
    print("addedge [node_a] [node_b]: (example: addedge 1 2) Adds a (directed) edge from node_a to node_b (Note that nodes are 0-indexed).")
    print("deledge [node_a] [node_b]: (example: deledge 1 2) Deletes a (directed) edge (if it exists) from node_a to node_b (Note that nodes are 0-indexed).")
    print("resetgraph: Resets the current graph to the default graph.")
    print("")

# Main function
def main():
    # print help message on first execution
    print_help()
    # sets a persistent current_graph variable
    current_graph = load_default_graph()
    while True: # infinite loop
        print("Type in command to execute, or \"help\" for a list of available commands!")
        cmd = input()
        # splits input into an array of tokens by spaces
        args = cmd.split(" ")
        # command is the first argument
        cmd = args[0]
        # the other arguments are actual arguments
        args = args[1:]
        # on one hand why does python have no switch statements
        # on the other hand in C i'd be using strncmp so this is also not that bad actually
        if(cmd == "help"):
            print_help();
        elif(cmd == "resetgraph"):
            current_graph = load_default_graph();
        elif(cmd == "showgraph"):
            plt.clf();
            nx.draw(current_graph, with_labels = True);
            plt.show();
            print("")
        elif(cmd == "addedge"):
            if(len(args) < 2):
                print("addedge requires 2 arguments!")
            else:
                try:
                    current_graph.add_edge(int(args[0]), int(args[1]))
                    print("Successfully added edge!")
                # if int() fails, arguments isn't an integer, show user an error
                except ValueError:
                    print("Edge indices must be an integer!")
            print("")
        elif(cmd == "deledge"):
            if(len(args) < 2):
                print("deledge requires 2 arguments!")
            else:
                try:
                    current_graph.remove_edge(int(args[0]), int(args[1]))
                    print("Successfully deleted edge!")
                # if int() fails, arguments isn't an integer, show user an error
                except ValueError:
                    print("Edge indices must be an integer!")
                except nx.NetworkXError:
                    print("No edge found between nodes {} and {} to remove!".format(int(args[0]), int(args[1])));
            print("")
        elif(cmd == "exit"):
            print("Exiting program!");
            break;
        else:
            print("Command not recognized!");
            break;

# Boilerplate to make Python behave more like C or Java by making it have a main function
if __name__ == "__main__":
    main()
