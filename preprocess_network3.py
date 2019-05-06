"""
Convert Hafez poems to directed graph

-- Homework 3
-- Morteza ZAKERI
"""

import sys
import os
import io
import csv
import networkx as nx
import matplotlib.pyplot as plt


def convert_txt_to_id():
    path_txt = 'dataset/network_3/hafez_poem_1.txt'
    with io.open(path_txt, encoding='utf-8') as f:
        lines = f.readlines()
        tex = f.read()

    # words = tex.split(' ')
    # print('corpus tex:', len(tex))  # == n

    total_words_list = list()
    total_line_list = list()
    for line in lines:
        line = line.replace('\u200c', '')
        line = line.replace('\t', ' ')
        line = line.replace('\n', ' ')
        line_parts = line.split(' ')

        while line_parts.count(''):
            line_parts.remove('')

        total_line_list.append(line_parts)
        total_words_list += line_parts

    while total_words_list.count(''):
        total_words_list.remove('')

    index_list = list(set(total_words_list))
    print('corpus :', total_words_list[:-5])
    print('vocabulary :', index_list[:-5])
    print('corpus size :', len(total_words_list))
    print('vocabulary size:', len(index_list))  # == |V|< n^2

    symbol_indices = dict((s, i) for i, s in enumerate(index_list))
    indices_symbol = dict((i, s) for i, s in enumerate(index_list))
    print('symbol_indices', list(symbol_indices.values())[:-5])
    print('indices_symbol', list(indices_symbol.values())[:-5])

    print('total_line_list', total_line_list[:-2])
    graph = ''
    for one_beyt in total_line_list:
        i = 0
        while i < len(one_beyt)-1:
            graph += str(one_beyt[i]) + ',' + str(one_beyt[i+1]) + '\n'
            i += 1
    with io.open(path_txt[:-3]+'_graph_vocabulary.txt', mode='w', encoding='utf-8') as f:
        f.write(graph)


def main(argv):
    convert_txt_to_id()


if __name__ == '__main__':
    main(sys.argv)
