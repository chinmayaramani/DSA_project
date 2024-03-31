import matplotlib.pyplot as plt
import networkx as nx

# Define the graph
G = nx.Graph()

# Add nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']
G.add_nodes_from(nodes)

# Add edges with weights
edges = [('A', 'B', 6), ('A', 'F', 5),
         ('B', 'C', 5), ('B', 'G', 6),
         ('C', 'D', 7), ('C', 'H', 5),
         ('D', 'E', 7), ('D', 'I', 8),
         ('E', 'I', 15),
         ('F', 'G', 8), ('F', 'J', 7),
         ('G', 'H', 9), ('G', 'K', 8),
         ('H', 'I', 12), ('H', 'L', 10),
         ('I', 'N', 9),
         ('J', 'K', 5), ('J', 'O', 7),
         ('K', 'L', 7),
         ('L', 'M', 7), ('L', 'P', 13),
         ('M', 'N', 9),
         ('N', 'R', 7),
         ('O', 'P', 13), ('O', 'S', 9),
         ('P', 'Q', 8),
         ('Q', 'R', 9), ('Q', 'T', 11),
         ('R', 'W', 10),
         ('S', 'T', 9),
         ('T', 'U', 8),
         ('U', 'V', 8),
         ('V', 'W', 5)]

for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, width=6)

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

# edge weight labels
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# display
plt.axis('off')
plt.show()