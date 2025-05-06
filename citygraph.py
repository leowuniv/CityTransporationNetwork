# Graph

import heap

class Graph:
  def __init__(self):
    # Dictionary to store adjacency list with weights
    self.adj_list = {}
    self.edges = []
    
  def addVertex(self, vertex):
    # Add a vertex if it does not already exist
    if vertex not in self.adj_list:
      self.adj_list[vertex] = []

  def addEdge(self, vertex1, vertex2, weight=1):
    # Add weighted edge between V1 and V2 (Undirected Graph)
    if vertex1 in self.adj_list and vertex2 in self.adj_list:
      self.adj_list[vertex1].append([vertex2, weight])
      self.adj_list[vertex2].append([vertex1, weight])
      self.edges.append((weight, vertex1, vertex2))
    else:
      raise ValueError("Both vertices must exist in the graph.")

  # def dijkstra(self, startVert): # greedy algorithms not needed

  def display(self):
    # Display adjacency list
    for vertex, edges in self.adj_list.items():
      print(f"{vertex}: {edges}")

  def bfs():

  def dfs():

