import sys
import os
import io
import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


G = nx.read_weighted_edgelist('cdn982_hw03_dataset.txt', delimiter=' ')
A = nx.to_numpy_matrix(G)
e = np.linalg.eigvals(A)

print(max(e))
