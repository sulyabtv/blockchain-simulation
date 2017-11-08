# Blockchain Simulation, written in Python3
# To cut the tedious part of configuring parameters, use indirection : <sample_input

import numpy
import math
import heapq


def getshortestpathlengths(adj_graph):
    nvertices = numpy.shape(adj_graph)[0]
    min_distances = numpy.full((nvertices, nvertices), math.inf)
    for src in range(nvertices):
        visited = [False for x in range(nvertices)]
        min_distances[src][src] = int(0)
        visited[src] = True
        pq = [[0, src]]
        heapq.heapify(pq)
        while pq:
            dist = pq[0][0]
            vert = pq[0][1]
            pq = pq[1:]
            for j in range(nvertices):
                if visited[j] or adj_graph[vert][j] == -1:
                    continue
                if min_distances[src][j] > dist + adj_graph[vert][j]:
                    min_distances[src][j] = dist + adj_graph[vert][j]
                    pq.append([min_distances[src][j], j])
            heapq.heapify(pq)
            visited[vert] = True
    int_min_distances = numpy.zeros((nvertices, nvertices), dtype=int)
    for i in range(nvertices):
        for j in range(nvertices):
            int_min_distances[i][j] = int(min_distances[i][j])
    return int_min_distances


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

min_distances = getshortestpathlengths(adj_graph)

# print(adj_graph)
# print(nodes_tx_interval)
# print(miners_hashes_per_second)
# print(min_distances)
