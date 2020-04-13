"""
-- Assignment #6;
---Simulating two epidemic models on two network models

-- Morteza ZAKERI
--- m-zakeri.ir
--- m-zakeri@live.com
--- @mztel

-- Semester 1397-98 (Spring 2019)
-- Last update: 13980312
"""

from __future__ import unicode_literals

_author__ = 'Morteza ZAKERI'
__version__ = '0.1'

import sys
import os
import io
import csv
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt

import ndlib.models.epidemics.SIRModel as sir
import ndlib.models.epidemics.SISModel as sis

import ndlib.models.epidemics.SEISModel as seis


def generate_graph():
    from basic_statistics import extract_statistics
    print('network1_erdos_renyi_graph')
    erdos_renyi_graph = nx.erdos_renyi_graph(1000, 0.1)
    nx.write_edgelist(erdos_renyi_graph, 'diffusion/erdos_renyi_graph_1000')
    print('network1_erdos_renyi_graph extract_statistics')
    extract_statistics(path=None, G=erdos_renyi_graph)

    print('network2_barabasi_albert_graph')
    barabasi_albert_graph = nx.generators.barabasi_albert_graph(n=1000, m=50)
    nx.write_edgelist(G=barabasi_albert_graph, path='diffusion/barabasi_albert_graph_1000')
    print('network2_barabasi_albert_graph extract_statistics')
    extract_statistics(path=None, G=barabasi_albert_graph)


def sir_simulation(path=None, G=None):
    # Network Model Definition
    # G = nx.erdos_renyi_graph(1000, 0.1)
    if G is None:
        # G = nx.read_edgelist(path, create_using=nx.Graph)
        G = nx.generators.erdos_renyi_graph(n=500, p=0.1)
    # Model Selection
    model = sir.SIRModel(G)

    # Model Configuration
    import ndlib.models.ModelConfig as mc
    config = mc.Configuration()
    # beta: The infection rate (float value in [0,1])
    # gamma: The recovery rate (float value in [0,1])
    config.add_model_parameter('beta', 0.001)
    config.add_model_parameter('gamma', 0.01)
    # config.add_model_parameter("fraction_infected", 0.1)
    config.add_model_parameter("percentage_infected", 0.02)
    model.set_initial_status(config)

    # Simulation
    iterations = model.iteration_bunch(2000)
    trends = model.build_trends(iterations)

    # Visualize the results
    from bokeh.io import output_notebook, show
    from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend

    viz = DiffusionTrend(model, trends)
    p = viz.plot(width=800, height=500)
    show(p)

    # The prevalence plot captures the variation (delta) of nodes for each status in consecutive iterations.
    from ndlib.viz.bokeh.DiffusionPrevalence import DiffusionPrevalence

    # viz2 = DiffusionPrevalence(model, trends)
    # p2 = viz2.plot(width=500, height=500)
    # show(p2)

    # Multiple plots can be combined in a multiplot to provide a complete description of the diffusive process
    # from ndlib.viz.bokeh.MultiPlot import MultiPlot
    # vm = MultiPlot()
    # vm.add_plot(p)
    # vm.add_plot(p2)
    # m = vm.plot()
    # show(m)


# SIS:In this model, during the course of an epidemics,
# a node is allowed to change its status from Susceptible (S) to Infected (I).
def sis_simulation(path=None, G=None):
    # Network Model Definition
    # G = nx.erdos_renyi_graph(1000, 0.1)
    if G is None:
        G = nx.read_edgelist(path, create_using=nx.Graph)
    # Model Selection
    model = sis.SISModel(G)

    # Model Configuration
    import ndlib.models.ModelConfig as mc
    config = mc.Configuration()
    # beta: The infection rate (float value in [0,1])
    # lambda: The recovery rate (float value in [0,1])
    config.add_model_parameter('beta', 0.001)
    config.add_model_parameter('lambda', 0.01)
    # config.add_model_parameter("fraction_infected", 0.1)
    config.add_model_parameter("percentage_infected", 0.05)
    model.set_initial_status(config)

    # Simulation
    iterations = model.iteration_bunch(200)
    trends = model.build_trends(iterations)

    # Visualize the results
    from bokeh.io import output_notebook, show
    from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend

    viz = DiffusionTrend(model, trends)
    p = viz.plot(width=600, height=500)
    show(p)


def main(argv):
    """
    Set your network path and then run the code
    :param argv:
    :return:
    """
    network1_path = 'diffusion/erdos_renyi_graph_1000'
    network2_path = 'diffusion/barabasi_albert_graph_1000'
    real_network_path = 'dataset/network_3/hafez_poem_1._graph.txt'
    # generate_graph()
    sir_simulation(path=real_network_path, G=None)
    # sis_simulation(path=network2_path, G=None)


if __name__ == '__main__':
    main(sys.argv)
