"""
Compute the basic statistics for a given network

-- Homework 3
-- Morteza ZAKERI
"""

import sys
import os
import io
import csv
import networkx as nx
import matplotlib.pyplot as plt


def extract_statistics(path=None, G=None):
    if G is None:
        G = nx.read_edgelist(path, create_using=nx.Graph)
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


def main(argv):
    """
    Set your network path and then run the code
    :param argv:
    :return:
    """
    path_txt_net1 = 'dataset/network_1/Cit-HepPh.txt'
    path_txt_net2 = 'dataset/network_2/CA-HepPh.txt'
    path_txt_net3 = 'dataset/network_3/hafez_poem_1._graph.txt'
    extract_statistics(path_txt_net3)


if __name__ == '__main__':
    main(sys.argv)
