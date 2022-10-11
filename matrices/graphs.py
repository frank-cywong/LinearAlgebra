# Challenge -- Convert an Incidence Matrix to a NetworkX Graph
# 
# Write a program that converts an indcidence matrix into a NetworkX graph object, then draw the graph
# Bonus: First verify that the matrix is a legitimate incidence matrix first!
# Bonus: Write a program that converts a NetworkX graph object into an incidence matrix

# Import the NetworkX package for creating graphs, matplotlib.pyplot for plotting them
import networkx as nx
import matplotlib.pyplot as plt

# Makes presenting a table of data easier
from tabulate import tabulate

# Hard-coded Incidence matrix. Play around and make changes to test your program.
M = [[1,-1,0,0,0],[1,0,-1,0,0],[1,0,0,-1,0],[0,1,-1,0,0],[0,1,0,-1,0], [0,1,0,0,-1],[0,0,1,-1,0]]

#example_row_1 = [0,0,0,0,0,1,0,0,-1]
#example_row_2 = [0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

# A helpful piece of code:
# The index method return the index number of a element of a list

#print(example_row_1,example_row_1.index(1))
#print(example_row_2,example_row_2.index(-1))

#e = (example_row_1.index(1),example_row_2.index(-1))

#print(e)

def MtoG(A):
    G = nx.Graph();

    for row in M:
        rs = row.index(1);
        rd = row.index(-1);
        #print(rs);
        #print(rd);
        G.add_edge(rs,rd);
    return G;

def GtoM(G):
    A = [];
    nc = len(G.nodes());
    for e in G.edges():
        temp = [0] * nc; # ahhhh python syntax
        temp[e[0]] = 1;
        temp[e[1]] = -1;
        A.append(temp);
    return A

G = MtoG(M);

# NetworkX's draw function, which requires matplotlib.pyplot
nx.draw(G, with_labels = True, node_color="lightblue")

print("Close matplotlib to continue:");

# Need to tell pyplot to show the plot
plt.show()

A = GtoM(G);

print("Rebuilt incidence matrix from graph:");
print(tabulate(A));

print("DFS-based edge removal MST algorithm:");

nc = len(A[0]);

adjlist = [];

for i in range(nc):
    adjlist.append([]);

for i in range(len(A)):
    row = A[i];
    rs = row.index(1);
    rd = row.index(-1);
    adjlist[rs].append([rd, i]);
    adjlist[rd].append([rs, i]);
    #print(adjlist);

#print(adjlist);

visited = [False] * nc;

Q = [[0, -1]]; # jerry-rigged queue, also stores element of "edge" that led to this

A2 = [];

while(len(Q) != 0):
     curNode = Q.pop();
     inEdgeNum = curNode[1];
     curNode = curNode[0]; # types dont exist here
     if(visited[curNode]):
        continue;
     if(inEdgeNum != -1):
        A2.append(A[inEdgeNum]);
     visited[curNode] = True;
     for node in adjlist[curNode]:
         #print(node);
         if not visited[node[0]]:
            Q.append(node);

print("New incidence matrix:")
print(tabulate(A2));

G2 = MtoG(A2);
plt.clf();
nx.draw(G2, with_labels = True, node_color="lightblue");
plt.show();
