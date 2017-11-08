# Blockchain Simulation, written in Python3
# To cut the tedious part of configuring parameters, use indirection : <sample_input

import numpy

print("---------------------")
print("Blockchain Simulation")
print("---------------------")

# Parameter inputs
print("\nEnter the total number of nodes :")
num_nodes = int(input())

print("\nEnter the total number of miners :")
num_miners = int(input())
num_devices = num_nodes + num_miners

print("\nEnter the {}x{} adjacency matrix for the inter-device communication times in integers that denote simulated seconds. The network is modelled as an undirected weighted graph. The first {} vertices are nodes, and the rest {} are miners. If no edge is present, enter -1.".format(
    num_devices, num_devices, num_nodes, num_miners))
adj_graph = numpy.zeros((num_devices, num_devices), dtype=int)
for i in range(num_devices):
    for j in range(num_devices):
        adj_graph[i][j] = int(input())

nodes_tx_interval = []
print("\nFor each of the nodes, enter the interval between two transactions, in integers that denote simulated seconds.")
for i in range(num_nodes):
    nodes_tx_interval.append(int(input()))

miners_hashes_per_second = []
print("\nFor each of the miners, enter the hashes producable per second, in integers that denote simulated seconds.")
for i in range(num_miners):
    miners_hashes_per_second.append(int(input()))

# print(adj_graph)
# print(nodes_tx_interval)
# print(miners_hashes_per_second)
