import matplotlib.pyplot as plt
import networkx as nx

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
    #print("printgraph: Prints the current graph in the form of an adjacency matrix.") - not needed, use showgraph instead
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
    plt.show();
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
                # nx.networkXError is thrown when remove_edge can't find an edge to remove, in which case display this error
                except nx.NetworkXError:
                    print("No edge found between nodes {} and {} to remove!".format(int(args[0]), int(args[1])));
            print("")
        elif(cmd == "exit"):
            print("Exiting program!");
            break;
        elif(cmd == "startdfs"):
            print("Starting DFS visualization:");
            dfs_start(current_graph);
            print("DFS visualization complete!");
            print("");
        else:
            print("Command not recognized!");

# Boilerplate to make Python behave more like C or Java by making it have a main function
if __name__ == "__main__":
    main()
