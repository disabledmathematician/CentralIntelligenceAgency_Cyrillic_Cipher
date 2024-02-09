import networkx as nx
import matplotlib.pyplot as plt
# Copyright Charles Thomas Wallace Truscott, published on Github, Open Licence
def CharlesPlot():
	# 1, 2 & 3, 2, 4 & 5, 3, 6 & 7
	# 4, 8 & 9, 5, 10 & 11, 6, 12 & 13, 7, 14 & 15
#	plt.figure(0, dpi=150, figsize=[20, 20])
	plt.figure(0, dpi=120, figsize=[15, 15])
	plt.title("Charles. I love you Dad Mark Watters")
	g = nx.Graph()
	L = [1, 2, 3, 4, 5, 6, 7]
	L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
	L = [x for x in range(1, 64)]
	x = 0
	i, j = 1, 2
	while x < len(L) - (len(L) + 1) // 2:
		if x == 0:
			print(L[x], L[x + i], L[x + j])
			g.add_edge(L[x], L[x + i])
			g.add_edge(L[x], L[x + j])
		else:
			print(L[x], L[x + i], L[x + j])
			g.add_edge(L[x], L[x + i])
			g.add_edge(L[x], L[x + j])
		i += 1
		j += 1
		x += 1
		pos = nx.spring_layout(g, seed=7)  # positions for all nodes - seed for reproducibility

# nodes
	nx.draw_networkx_nodes(g, pos, node_color="red", node_size=700)

# edges
	nx.draw_networkx_edges(g, pos, width=6)
	nx.draw_networkx_edges(
    g, pos, width=6, alpha=0.5, edge_color="grey", style="dashed"
)

# node labels
	nx.draw_networkx_labels(g, pos, font_size=20, font_family="monospace")
	plt.savefig("luvudad2.png")
CharlesPlot()