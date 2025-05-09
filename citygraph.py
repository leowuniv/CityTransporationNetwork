# Graph
'''
Analysis is included below in a comment box
'''

import heap

class Graph:
  '''
  A class that uses adjacency lists or matrices to keep track of edges
  '''
  def __init__(self):
    # Dictionary to store adjacency list with weights
    self.adj_list = {}
    self.edges = []
    
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

  def bfs(self):
    '''
    This class for BFS prints out the order of landmarks visited
    '''
    visited = []
    '''
    1. Start by creating an empty set and Queue of vertices to visit,
    putting the source vertex in the queue and setting it as visited in
    the array.
    2.While the Queue is not empty:
    1. Take the front item of the queue and print it
    2. Add all its unvisited adjacent vertices to the back of the queue while
    also marking them as visited to avoid adding them again.
    '''

  def dfs(self):
    '''
    This class for DFS is using a stack to print out the order of landmarks visited
    '''
    visited = []
    '''
    1. Create new stack and Boolean array, start at source vertex
    and add it to stack.
    2. While the Stack is not empty:
    1. Pop a node from the stack to use
    2. If that node has not been visited, mark it as being visited and print
    the node
    3. For all non-visited adjacent nodes to the current node, push them
    onto the stack
    '''

def main(): # tester for city network
  # Create a method to instantiate a sample city network with at least 10 landmarks and 15 roads.
  # Demonstrate both BFS and DFS traversals starting from a given landmark.

if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------

# Analysis Portion
# ==========================================================================
'''
  After observing the works between BFS and DFS, we are able to indicate that BFS and DFS have distinct differences. To begin, in the context of our transportation network, BFS is...

  The scenarios in which we would prefer BFS over DFS is...


'''
