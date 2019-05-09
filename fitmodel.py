"""
Fit model

-- Assignment #4;
--- Network generation practice
-- Morteza ZAKERI
"""



import sys
import os
import io
import csv
import networkx as nx
import matplotlib.pyplot as p

from basic_statistics import extract_statistics


def fit1(path):
    """

    :param path:
    :return:
    """
    # G = nx.read_edgelist(path, create_using=nx.Graph)

    """
        1 Simulate network_1 with erdos_renyi model
    """
    # erdos_renyi_graph = nx.generators.erdos_renyi_graph(n=34546, p=0.0007)
    # nx.write_edgelist(G=erdos_renyi_graph, path='network_1_erdos_renyi_graph.txt')
    # extract_statistics(path=None, G=erdos_renyi_graph)

    """
        2 Simulate network_1 with watts_strogatz model
    """
    watts_strogatz_graph = nx.generators.watts_strogatz_graph(n=34546, k=24, p=0.01)  # MemoryError on my system!!!
    # watts_strogatz_graph = nx.generators.watts_strogatz_graph(n=34546/2, k=24/2, p=0.01)
    nx.write_edgelist(G=watts_strogatz_graph, path='network_1_watts_strogatz_graph.txt')
    extract_statistics(path=None, G=watts_strogatz_graph)
    """
        3 Simulate network_1 with barabasi_albert model
    """
    # barabasi_albert_graph = nx.generators.barabasi_albert_graph(n=34546, m=12)
    # nx.write_edgelist(G=barabasi_albert_graph, path='network_1_barabasi_albert_graph.txt')
    # extract_statistics(path=None, G=barabasi_albert_graph)


def fit2(path=None):
    """

    :param path:
    :return:
    """
    # G = nx.read_edgelist(path, create_using=nx.Graph)

    """
        1 Simulate network_2 with erdos_renyi model
    """
    # erdos_renyi_graph = nx.generators.erdos_renyi_graph(n=12008, p=0.0016)
    # nx.write_edgelist(G=erdos_renyi_graph, path='network_2_erdos_renyi_graph.txt')
    # extract_statistics(path=None, G=erdos_renyi_graph)

    """
        2 Simulate network_2 with watts_strogatz model
    """
    # watts_strogatz_graph = nx.generators.watts_strogatz_graph(n=12008, k=19, p=0.01)
    # nx.write_edgelist(G=watts_strogatz_graph, path='network_2_watts_strogatz_graph.txt')
    # extract_statistics(path=None, G=watts_strogatz_graph)
    """
        3 Simulate network_2 with barabasi_albert model
    """
    print('network_2_barabasi_albert_graph')
    barabasi_albert_graph = nx.generators.barabasi_albert_graph(n=12008, m=10)
    nx.write_edgelist(G=barabasi_albert_graph, path='network_2_barabasi_albert_graph.txt')
    extract_statistics(path=None, G=barabasi_albert_graph)


def fit3(path=None):
    """

    :param path:
    :return:
    """
    # G = nx.read_edgelist(path, create_using=nx.Graph)

    """
        1 Simulate network_3 with erdos_renyi model
    """
    # erdos_renyi_graph = nx.generators.erdos_renyi_graph(n=12025, p=0.0008)
    # nx.write_edgelist(G=erdos_renyi_graph, path='network_3_erdos_renyi_graph.txt')
    # extract_statistics(path=None, G=erdos_renyi_graph)

    """
        2 Simulate network_3 with watts_strogatz model
    """
    # watts_strogatz_graph = nx.generators.watts_strogatz_graph(n=12025, k=10, p=0.01)
    # nx.write_edgelist(G=watts_strogatz_graph, path='network_3_watts_strogatz_graph.txt')
    # extract_statistics(path=None, G=watts_strogatz_graph)
    """
        3 Simulate network_3 with barabasi_albert model
    """
    print('network3_barabasi_albert_graph')
    barabasi_albert_graph = nx.generators.barabasi_albert_graph(n=12025, m=5)
    nx.write_edgelist(G=barabasi_albert_graph, path='network_3_barabasi_albert_graph.txt')
    extract_statistics(path=None, G=barabasi_albert_graph)


def main(argv):
    path_txt_net1 = 'dataset/network_1/Cit-HepPh.txt'
    path_txt_net1_gc = 'dataset/network_1/Cit-HepPhgc.txt'
    path_txt_net2 = 'dataset/network_2/CA-HepPh.txt'
    path_txt_net3 = 'dataset/network_3/hafez_poem_1._graph.txt'

    print('-' * 50, 'Network 1')
    fit1(path_txt_net1_gc)
    # print('-' * 50, 'Network 2')
    # fit2(path_txt_net2)
    # print('-' * 50, 'Network 3')
    # fit3(path_txt_net3)


if __name__ == '__main__':
    main(sys.argv)
