import matplotlib.pyplot as plt
import networkx as nx
from tabulate import tabulate
import time

# A default / sample graph in adjacency matrix form
# A[i, j] is 1 if there is an edge connecting i to j
DEFAULT_GRAPH_ADJ = [[0, 1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0]];

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
    print("printgraph: Prints the current graph in the form of an adjacency matrix.")
    print("showgraph: Displays the current graph with Matplotlib.")
    print("addedge [node_a] [node_b]: (example: addedge 1 2) Adds a (directed) edge from node_a to node_b (Note that nodes are 0-indexed).")
    print("deledge [node_a] [node_b]: (example: deledge 1 2) Deletes a (directed) edge (if it exists) from node_a to node_b (Note that nodes are 0-indexed).")
    print("resetgraph: Resets the current graph to the default graph.")
    print("startdfs: Start DFS visualization")
    print("")


# Start DFS process
def dfs_start(graph):
    # initialize node stack with starting (root) node (id: 0)
    node_stack = [];
    node_stack.append(0);
    visited_arr = [];
    # initialize visited array to all false
    for i in range(len(graph)):
        visited_arr.append(False);
    dfs_wrapper(node_stack, visited_arr, graph);


def dfs_wrapper(node_stack, visited_arr, graph):
    # generate a graph layout
    layout = nx.spring_layout(graph);
    # do DFS until end
    while(dfs_step_with_draw(node_stack, visited_arr, graph, layout)):
        pass;
    # close plot
    plt.close();

# returns True if continue, False if end
def dfs_step_with_draw(node_stack, visited_arr, graph, pos):
    node_removed = dfs_step(node_stack, visited_arr, graph)
    # if no more nodes left to visit, end
    if(node_removed == None):
        return False
    node_count = len(graph)
    not_visited_stack = []
    visited_stack = []
    for i in range(node_count):
        if(i == node_removed):
            continue;
        # if i is visited, put it in a stack (needed for drawing the graph)
        if(visited_arr[i]):
            visited_stack.append(i);
        # if i is neither visited or the node just visited, put it in the not visited stack
        else:
            not_visited_stack.append(i)
    plt.clf();
    nx.draw_networkx_edges(graph, pos, width=1.0);
    nx.draw_networkx_labels(graph, pos);
    # draw current node
    nx.draw_networkx_nodes(graph, pos, nodelist=[node_removed], node_color="tab:red");
    # draw not visited nodes
    nx.draw_networkx_nodes(graph, pos, nodelist=not_visited_stack, node_color="tab:blue");
    # draw visited nodes
    nx.draw_networkx_nodes(graph, pos, nodelist=visited_stack, node_color="tab:green");
    plt.pause(0.1);
    plt.show(block = False);
    time.sleep(1);
    plt.pause(0.1);
    return True

# Steps through 1 step of the DFS process
# node_stack is an array that is used as a stack, stores nodes to visit
# visited_arr is an array that tracks if node x was visited
# graph is the graph to modify
# Returns the current node for the purpose of graphing it
def dfs_step(node_stack, visited_arr, graph):
    # loop infinitely until we find a working node to test (or run out of nodes to test)
    while True:
        # Are there even any nodes left?
        if(len(node_stack) == 0):
            return None;
        # Most recently added node is the one we look at
        node_to_remove = node_stack.pop();
        # Check if we've visited this node already
        if(not visited_arr[node_to_remove]):
            break;

    # set current node to visited
    visited_arr[node_to_remove] = True;

    # Iterate over all this node's neighbours and add them if they haven't been visited yet
    for adj_neighbour in graph.neighbors(node_to_remove):
        if(not visited_arr[adj_neighbour]):
            node_stack.append(adj_neighbour)

    return node_to_remove;

# Imports a graph from a user-input adjacency matrix
def import_graph():
    print("Input number of nodes (ie. size of adjacency matrix):")
    matrix_storage = []
    node_count = int(input());
    print("Input adjacency matrix, all elements should be 0 or 1 with spaces between elements, and a newline per row.")
    print("Note that the 1st (0th) node will be the start node for the depth first search.")
    # Iterate through every row
    for i in range(node_count):
        row_string = input();
        row_arr = row_string.split(" ");
        row_int_arr = [];
        if(len(row_arr) != node_count):
            print("Error: Input must be square, number of elements in row does not match node count!");
            return None
        # Convert value for each element in each row to number, must be 0 or 1
        for j in range(node_count):
            try:
                cur_val = int(row_arr[j]);
                if(cur_val != 0 and cur_val != 1):
                    print("Error: Each element in adjacency matrix must be 0 or 1!");
                    return None;
                row_int_arr.append(cur_val)
            except:
                print("Error: Each element in adjacency matrix must be 0 or 1!");
                return None;
        matrix_storage.append(row_int_arr)
    try:
        G = load_graph_from_adj_matrix(matrix_storage)
        return G
    except:
        return None

# Prints a graph as an adjacency matrix
def print_graph(graph):
    # Step 1: Convert graph to adjacency matrix
    matrix = [];
    for i in range(len(graph)):
        adj_nodes = graph[i];
        currow = [];
        for j in range(len(graph)):
            if(j in adj_nodes):
                currow.append(1);
            else:
                currow.append(0);
        matrix.append(currow);
    # Step 2: Print the resulting adjacency matrix
    print(tabulate(matrix));

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
            print("Graph shown, will auto-close in 5 seconds");
            plt.pause(0.1);
            plt.show(block = False);
            plt.pause(0.1);
            time.sleep(5);
            plt.close();
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
                # nx.networkXError is thrown when remove_edge can't find an edge to remove, in which case display this error
                except nx.NetworkXError:
                    print("No edge found between nodes {} and {} to remove!".format(int(args[0]), int(args[1])));
            print("")
        elif(cmd == "exit"):
            print("Exiting program!");
            break;
        elif(cmd == "startdfs"):
            print("Starting DFS visualization:");
            print("Blue -> Unvisited nodes");
            print("Red -> Current node");
            print("Green -> Visited nodes");
            dfs_start(current_graph);
            print("DFS visualization complete!");
            print("");
        elif(cmd == "importgraph"):
            potential_new_graph = import_graph();
            if(potential_new_graph != None):
                print("Graph imported!");
                current_graph = potential_new_graph
            print("")
        elif(cmd == "printgraph"):
            print_graph(current_graph);
            print("")
        else:
            print("Command not recognized!");
            print("");

# Boilerplate to make Python behave more like C or Java by making it have a main function
if __name__ == "__main__":
    main()
