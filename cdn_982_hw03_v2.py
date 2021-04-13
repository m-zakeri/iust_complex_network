import sys
import os
import io
import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math


# e = np.linalg.eigvals([[1, -2], [-2, 0]])

# print(e)
# print('max', max(e))
# print('test', (1+math.sqrt(17)) / 2)

path = 'cdn982_hw03_dataset.txt'
path = 'dataset/snap.stanford.edu/DD-Miner_miner-disease-disease.tsv'
G = nx.read_weighted_edgelist(path, delimiter='\t', create_using=nx.DiGraph)
A = nx.to_numpy_matrix(G)
print('compute eigvals')
e = np.linalg.eigvals(A)
print(e)
print(max(e))

