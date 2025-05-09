# Graph
'''
Analysis is included below in a comment box
'''

import heapq

class Graph:
  '''
  A class that uses adjacency lists or matrices to keep track of edges
  '''
  def __init__(self):
    # Dictionary to store adjacency list with weights
    self.adj_list = {} # nodes = landmarks
    self.edges = [] # edges = roads in between the landmarks
    
  def addVertex(self, vertex):
    '''
    Adds a vertex to graph
    '''
    # Add a vertex if it does not already exist
    if vertex not in self.adj_list:
      self.adj_list[vertex] = []

  # Ensure that your graph can handle String identifiers for vertices.

  def addEdge(self, vertex1, vertex2, weight=1):
    '''
    Adds edge
    '''
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

  def bfs(self, startVert):
    '''
    This class for BFS prints out the order of landmarks visited
    '''
    visited = set()
    # our queue for vertices to visit
    notVisited:list = [startVert]

    while len(notVisited) > 0:
      vert = notVisited.pop()
      visited.add(vert)
      print(vert)
      for vert in self.adj_list[vert]:
        if vert not in visited:
            notVisited.insert(0,vert)

  def dfs(self, startVert):
    '''
    This class for DFS is using a stack to print out the order of landmarks visited
    '''
    visited = set()
    # our stack for vertices to visit
    notVisited:list = [startVert]

    while len(notVisited) > 0:
      vert = notVisited.pop()
      visited.add(vert)
      print(vert)
      for vert in self.adj_list[vert]:
        if vert not in visited:
            notVisited.append(vert)

def main(): # tester for city network
  # Create a method to instantiate a sample city network with at least 10 landmarks and 15 roads.
  # Demonstrate both BFS and DFS traversals starting from a given landmark.
  cityNetwork = Graph()
  #landmarks (10)
  cityNetwork.addVertex("Grand Library of All Books")
  cityNetwork.addVertex("Harvard University")
  cityNetwork.addVertex("Charles River")
  cityNetwork.addVertex("Harvard Square")
  cityNetwork.addVertex("Harvard Museum of Natural History & Arts")
  cityNetwork.addVertex("MIT")
  cityNetwork.addVertex("Automated McDonalds")
  cityNetwork.addVertex("Starbucks")
  cityNetwork.addVertex("Grocery Store")
  cityNetwork.addVertex("Subway Metro Station")
  #roads (20)
  cityNetwork.addEdge("Grand Library of All Books", "Harvard University")
  cityNetwork.addEdge("Grand Library of All Books", "Charles River")
  cityNetwork.addEdge("Grand Library of All Books", "MIT")
  cityNetwork.addEdge("Grand Library of All Books", "Harvard Square")
  cityNetwork.addEdge("Grand Library of All Books", "Harvard Museum of Natural History & Arts")
  
  cityNetwork.addEdge("Harvard University", "Harvard Square")
  cityNetwork.addEdge("Harvard University", "Harvard Museum of Natural History & Arts")
  cityNetwork.addEdge("Harvard University", "Grand Library of All Books")
  cityNetwork.addEdge("Harvard University", "Starbucks")
  cityNetwork.addEdge("Harvard University", "Subway Metro Station")
  
  cityNetwork.addEdge("MIT", "Grand Library of All Books")
  cityNetwork.addEdge("Grocery Store", "Automated McDonalds") # error testing if Mcdonalds lower case won't work
  cityNetwork.addEdge("Automated McDonalds", "Charles River")
  cityNetwork.addEdge("MIT", "Starbucks")
  cityNetwork.addEdge("MIT", "Subway Metro Station")
  
  cityNetwork.addEdge("Subway Metro Station", "Grocery Store")
  cityNetwork.addEdge("Subway Metro Station", "Automated McDonalds")
  cityNetwork.addEdge("Subway Metro Station", "Harvard University")
  cityNetwork.addEdge("Subway Metro Station", "MIT")
  cityNetwork.addEdge("Subway Metro Station", "Charles River")
  
  cityNetwork.display()
  

if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------

# Analysis Portion
# ==========================================================================
'''
  After observing the works between BFS and DFS, we are able to indicate that BFS and DFS have distinct differences. To begin, in the context of our transportation network, BFS is...

  The scenarios in which we would prefer BFS over DFS is...


'''
