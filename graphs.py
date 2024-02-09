import networkx as nx
import matplotlib.pyplot as plt

def Charles():
	plt.figure(0, dpi=150, figsize=[10, 10])
	plt.title("Charles Truscott Watters. I love you Dad")
	g = nx.Graph()
	g.add_edge("A", "B", weight = 19)
	g.add_edge("A", "C", weight = 55)
	g.add_edge("C", "B", weight = 2)
	g.add_edge("B", "D", weight = 4)
	g.add_edge("C", "E", weight = 8)
	g.add_edge("D", "F", weight = 1)
	g.add_edge("E", "F", weight = 19)
	g.add_edge("D", "C", weight = 93)
	edge_labels = nx.get_edge_attributes(g, "weight")
	
	pos = nx.spring_layout(g, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
	nx.draw_networkx_nodes(g, pos, node_color="pink", node_size=700)

# edges
	nx.draw_networkx_edges(g, pos, width=6)
	nx.draw_networkx_edges(
    g, pos, width=6, alpha=0.5, edge_color="pink", style="dashed"
)

# node labels
	nx.draw_networkx_labels(g, pos, font_size=20, font_family="monospace")
# edge weight labels
	edge_labels = nx.get_edge_attributes(g, "weight")
	nx.draw_networkx_edge_labels(g, pos, edge_labels)
#	pos = nx.spring_layout(g)
#	nx.draw_networkx_edge_labels(g, pos, edge_labels)
	plt.show()
#	nx.draw(g, with_labels=True)
#	plt.savefig("charles.png")
Charles()
	