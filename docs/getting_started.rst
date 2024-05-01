Getting Started
===============

This page details how to get started with molecool. 

Requirments
=============
numpy


Using molecool
==============
an example of using molecool to calculate the average Energy, Magnetization, Heat Capacity,
and Magnetization Susceptibility of a 6 site hexagon shaped lattice with edge weight 1, at 1 kelvin

::

    import molecool
    import numpy as np
    import networkx as nx

    #number of sites
    n = 6
    #temperature (in kelvin)
    T = 1
    #weight of each edge
    w = 1

    G = nx.Graph()
    G.add_nodes_from([i for i in range(n)])
    #adds edges of bodering sites, forming a hexagon
    G.add_edges_from([(i,(i+1)% G.number_of_nodes() ) for i in range(n)])

    J = [[] for i in G.nodes()]
    for e in G.edges:
        #creates a list of tuples, storing the nodes of the connection and weight
        J[e[0]].append((e[1], w))
        J[e[1]].append((e[0], w))

    ham = molecool.IsingHamiltonian(n, J,mus)

    Energy, Magnetization, Heat_Capacity, Magnetization_Sucsceptibility = ham.compute_average_values(T)