#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Charles Truscott Watters
 
 I was searching for efficient code abstractions to describe graph theoretic algorithms 
 that are beneficial toward reducing visualisations, and in the same providing great
 tree call structures for dynamic programming or tree-diagram solution to computational
 problems. Including networkx and matplotlib visualisations in my neat little solution,
 but also is valid for the same computational solution structure described by the tree.
 Next a trinary tree and a kilominute interval between hypothetical indices structure
 of weights of randomly-generated stock prices, and a random walk through the tree
 (Can the true walk through a financial optimisation tree become a spanning tree out of all other hypothetical walks?)
 Charles Thomas Wallace Truscott Watters. 127 Broken Head Rd, Suffolk Park, NSW 2481
 
"""
import networkx as nx
import matplotlib.pyplot as plt

def Plot():
    n = 8
    count = 2
    while count < 16:
        plt.figure(count, dpi=120, figsize=[12, 12])
        L = [x for x in range(1, 2 ** count)]
        i, j = 1, 2
        x = 0
        G = nx.Graph()
        while x < (len(L) - ((len(L) + 1) // 2)):
            G.add_edge(L[x], L[x + i])
            G.add_edge(L[x], L[x + j])
            i += 1
            j += 1
            x += 1
        plt.title("Charles Truscott Watters.".format(count))
        pos = nx.spring_layout(G, seed=5)
        nx.draw_networkx_nodes(G, pos, node_color='red', node_size=120)
        nx.draw_networkx_edges(G, pos, width=0.5)
        nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.5, edge_color='grey', style='dashed')
        plt.savefig("CharlesTruscottWatters-{}.png".format(count))
        count += 1

def CharlesTruscott():
    Plot()
    
CharlesTruscott()

