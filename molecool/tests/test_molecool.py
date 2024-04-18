"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import molecool

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "molecool" in sys.modules

def test_molecool_compute_average_values():
    """Test to confirm compute average values returns correct values"""
    #creates hexagon graph with edge weight 2
    G = nx.Graph()
    G.add_nodes_from([i for i in range(6)])
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(6)])
    for e in G.edges:
        G.edges[e]['weight'] = 2

    #turns graph into IsingHamiltonian object
    J = [[] for i in G.nodes()]
    for e in G.edges:
        J[e[0]].append((e[1], G.edges[e]['weight']))
        J[e[1]].append((e[0], G.edges[e]['weight']))
    ham = molecool.IsingHamiltonian(6, J,np.zeros(6))

    E, M, HC, MS = ham.compute_average_values(1)
    assert(np.isclose(E,  -11.95991923))
    assert(np.isclose(M,   -0.00000000))
    assert(np.isclose(HC,   0.31925472))
    assert(np.isclose(MS,   0.01202961))