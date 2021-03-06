"""
==============
Weighted Graph
==============

An example using Graph as a weighted network.
"""
import matplotlib.pyplot as plt
import networkx as nx


G = nx.Graph()

G.add_edge("a", "b", weight=2)
G.add_edge("a", "g", weight=5)
G.add_edge("a","d",weight =2)
G.add_edge("b","e",weight =4)
G.add_edge("b", "d", weight=7)
G.add_edge("d", "e", weight=7)
G.add_edge("e","f",weight =8)
G.add_edge("f","g",weight =4)



elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 5]

pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(
    G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)



# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
print("graf keberangkatan b ke f")
print(elarge)
print("graf kembali dari f ke b")
print(esmall)
plt.axis("off")
plt.show()
