"""
Compute the basic statistics for a given network

-- Homework 3
-- Morteza ZAKERI
"""
from __future__ import unicode_literals

import sys
import os
import io
import csv
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt

from bidi.algorithm import get_display
import arabic_reshaper


# Assignment #3
def extract_statistics(path=None, G=None):
    if G is None:
        G = nx.read_edgelist(path, create_using=nx.Graph)

    # visualize_graph(graph=G)

    # nx.algorithms.community.asyn_lpa_communities
    print('number_of_nodes', nx.number_of_nodes(G))
    print('number_of_edges', nx.number_of_edges(G))
    print('number_of_selfloops', nx.number_of_selfloops(G))

    sum_degrees = 0
    for i in nx.degree(G):
        sum_degrees += i[1]

    print('average_degree', sum_degrees / float(len(G)))

    # print('average_neighbor_degree', nx.average_neighbor_degree(G))
    #print('average_degree_connectivity', nx.average_degree_connectivity(G))
    # print('average_node_connectivity', nx.average_node_connectivity(G))
    print('density', nx.density(G))

    # Just for directed graphs
    # print('condensation', nx.condensation(G))

    # Clustering coefficient 1 (Transitivity)
    print('Transitivity', nx.transitivity(G))
    # Clustering coefficient 2 (CC)
    print('Clustering coefficient 2', nx.average_clustering(G))

    print('degree_assortativity_coefficient', nx.degree_assortativity_coefficient(G))
    print('degree_pearson_correlation_coefficient', nx.degree_pearson_correlation_coefficient(G))

    print('degree_centrality', sorted(nx.degree_centrality(G).items(), key=lambda kv: (kv[1], kv[0]))[:10])

    # print('closeness_centrality', nx.closeness_centrality(G))
    # print('betweenness_centrality', nx.betweenness_centrality(G))


    print('is_connected', nx.is_connected(G))
    print('number_connected_components', nx.number_connected_components(G))
    if nx.is_connected(G):
        print('diameter', nx.diameter(G))
        print('average_shortest_path_length', nx.average_shortest_path_length(G))
    else:
        # ccs_asp_list = []
        # ccs_d_list = []
        # print('number_connected_components', nx.number_connected_components(G))
        # for g in nx.connected_component_subgraphs(G):
        #     ccs_d_list.append(nx.average_shortest_path_length(g))
        #     ccs_asp_list.append(nx.average_shortest_path_length(g))

        Gc = max(nx.connected_component_subgraphs(G), key=len)
        print('***wait*** ...')
        print('max_cc_asp', nx.average_shortest_path_length(Gc))
        print('max_cc_diameter', nx.diameter(Gc))

    print('end')

    # print('katz_centrality', nx.katz_centrality(G))

    # Gr = nx.Graph()
    # Gr.number_of_selfloops()


# Assignment #4
def extract_giant_connected_component(path=None, G=None):
    if G is None:
        G = nx.read_edgelist(path, create_using=nx.Graph, delimiter='\t', nodetype=int, encoding='utf8')
    print('is_connected', nx.is_connected(G))
    print('number_connected_components', nx.number_connected_components(G))
    if nx.is_connected(G) is False:
        print('***wait*** ...')
        giant_connected_component = max(nx.connected_component_subgraphs(G), key=len)
        nx.write_edgelist(giant_connected_component, path=path[:-4]+'gc.txt')
    print('Giant connected Component is extracted.')


# Assignment #5
def community_detection(path=None, G=None):
    """
    Modularity Maximization Algorithm
    :param path:
    :param G:
    :return:
    """
    if G is None:
        G = nx.read_edgelist(path, create_using=nx.Graph)
    # nx.algorithms.community.girvan_newman()

    # G = nx.karate_club_graph()
    c = list(nx.algorithms.community.greedy_modularity_communities(G))
    print('Communities:', c)
    print('Number of communities:', len(c))

    Q = nx.algorithms.community.modularity(G, c)
    print('Modularity:', Q)

# Assignment #3
def visualize_graph(graph):
    """

    :param graph:
    :return:
    """
    # matplotlib.rc('font', family='B Nazanin')
    matplotlib.rc('font', **{'sans-serif': 'Arial', 'family': 'sans-serif'})

    font_title = {'family': 'B Nazanin',
                  'color': 'red',
                  'weight': 'normal',
                  'size': 12,
                  }
    font_labels = {'family': 'B Nazanin',
                   'color': 'black',
                   'weight': 'normal',
                   'size': 12,
                   }

    # print(nx.nodes)
    # new_names_dict = dict()
    # for node_name in nx.nodes(graph):
    #     print(node_name)
        # new_names_dict.update({node_name: make_farsi_text(node_name)})

    # nx.relabel_nodes(graph, mapping=new_names_dict)
    subgraph = nx.subgraph(graph, nbunch=list(nx.nodes(graph))[:1000])
    # nx.draw(subgraph, node_size=0, alpha=0.4, edge_color='r', font_size=11, with_labels=True)

    new_names_dict = dict()
    for node_name in nx.nodes(subgraph):
        # print(node_name)
        new_names_dict.update({node_name: make_farsi_text(node_name)})

    # pos = nx.spring_layout(subgraph)
    # pos = nx.circular_layout(subgraph)
    ## pos = nx.rescale_layout(subgraph)
    # pos = nx.random_layout(subgraph)
    # pos = nx.spectral_layout(subgraph)

    pos = nx.kamada_kawai_layout(subgraph)

    # pos = nx.fruchterman_reingold_layout(subgraph)
    # pos = nx.shell_layout(subgraph)
    ## pos = nx.bipartite_layout(subgraph)


    nx.draw_networkx_nodes(subgraph, pos, nodelist=list(nx.nodes(subgraph)), node_color='r', node_size=2, alpha=0.1)

    nx.draw_networkx_edges(subgraph, pos, edgelist=list(nx.edges(subgraph)), width=0.9, alpha=0.2, edge_color='b')

    nx.draw_networkx_labels(subgraph, pos, new_names_dict, font_family='B Nazanin', font_size=12)

    plt.show()


def make_farsi_text(x):
    reshaped_text = arabic_reshaper.reshape(x)
    farsi_text = get_display(reshaped_text)
    print(farsi_text)
    return farsi_text


def main(argv):
    """
    Set your network path and then run the code
    :param argv:
    :return:
    """
    path_txt_net1 = 'dataset/network_1/Cit-HepPh.txt'
    path_txt_net1_gc = 'dataset/network_1/Cit-HepPhgc.txt'
    path_txt_net2 = 'dataset/network_2/CA-HepPh.txt'
    path_txt_net3 = 'dataset/network_3/hafez_poem_1._graph.txt'
    path_txt_net3_v = 'dataset/network_3/hafez_poem_1._graph_vocabulary.txt'
    extract_statistics(path_txt_net1_gc)
    extract_giant_connected_component(path=path_txt_net1)
    community_detection(path_txt_net1_gc)


if __name__ == '__main__':
    main(sys.argv)
