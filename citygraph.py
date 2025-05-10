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
    # Add weighted edge between V1 and V2 for (Undirected Graph); Directed graph need 1 edge
    if vertex1 in self.adj_list and vertex2 in self.adj_list:
      self.adj_list[vertex1].append([vertex2, weight])
      #self.adj_list[vertex2].append([vertex1, weight])
      self.edges.append((weight, vertex1, vertex2))
    else:
      raise ValueError("Both vertices must exist in the graph.")

  def display(self):
    # Display adjacency list
    for vertex, edges in self.adj_list.items():
      print(f"{vertex}: {edges}")

  def bfs(self, startVert):
    '''
    This method for BFS prints out the order of landmarks visited
    '''
    visited = set()
    # our queue for vertices to visit
    notVisited:list = [startVert]

    while len(notVisited) > 0:
      vert = notVisited.pop()
      visited.add(vert)
      print(vert)
      for adjVert, _ in self.adj_list[vert]:
        if adjVert not in visited:
            notVisited.insert(0,adjVert)
            visited.add(adjVert)

  def dfs(self, startVert):
    '''
    This method for DFS is using a stack to print out the order of landmarks visited
    '''
    visited = set()
    # our stack for vertices to visit
    notVisited:list = [startVert]

    while len(notVisited) > 0:
      vert = notVisited.pop()
      visited.add(vert)
      print(vert)
      for adjVert, _ in self.adj_list[vert]:
        if adjVert not in visited:
            notVisited.append(adjVert)
            visited.add(adjVert)

  def dijkstra(self, startVert) -> dict:
    '''
    Dijkstra used to find the shortest distance to vertices from the start vertex.
    '''
    # TODO make sure there are valid edges to traverse through
    if startVert not in self.adj_list:
      raise ValueError("Both vertices must exist in the graph.")
    
    # track w/ heap the next closest to visit
    pq = []
    heapq.heappush(pq, (0, startVert))
    dists = {vertex: float("inf") for vertex in self.adj_list}
    # ordered keys for which vertex to pass through
    dists[startVert] = 0
    visited = set()
    while pq:
      currentDistance, vertex = pq.pop()

      if vertex in visited:
        continue
      visited.add(vertex)

      for adjacentVertex, dist in self.adj_list[vertex]:
        if adjacentVertex not in visited:
          # neighbor distance through current vertex
          newDistance = currentDistance + dist
          if newDistance < dists[adjacentVertex]:
            # if smaller distance than previous, add it to path
            dists[adjacentVertex] = newDistance
            heapq.heappush(pq, (newDistance, adjacentVertex))

    return dists

  def route(self, startVert, endVert) -> list: 
    '''
    This method uses Dijkstra's algoroithm to find the shortest path between two vertices.
    '''
    # Implement a function that uses BFS to find the shortest path (in terms of the number of edges) from one landmark to another if one exists.
    if endVert not in self.adj_list:
      raise ValueError("Both vertices must exist in the graph.")
    dists = self.dijkstra(startVert)
    shortestDistance = dists[endVert]
    predecessors = {vertex:None for vertex in self.adj_list}

    '''
    stops = [endVert]
    visited = set()
    toVisit = self.adj_list[endVert]
    currentDistance = shortestDistance
    '''
    for vertex, distance in dists.items():
      for adjacentVertex, dist in self.adj_list[vertex]:
        # check if the shortest distance to the neighbor from start is equal to shortest distance to current vertex + distance from current vertex to neighbor
        if dists[adjacentVertex] == distance + dist:
          # if shortest distance to neighbor is sum, then this vertex is the predecessor to the neighbor
          predecessors[adjacentVertex] = vertex
          # should be no predecessor to start

    # backtrace steps from end
    path = []
    currentVertex = endVert
    while currentVertex:
      path.insert(0,currentVertex)
      currentVertex = predecessors[currentVertex]
    
    return path

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
  #roads (15+)
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
  
  cityNetwork.addEdge("Charles River", "Subway Metro Station")
  cityNetwork.addEdge("Automated McDonalds", "Subway Metro Station")
  cityNetwork.addEdge("Grocery Store", "Subway Metro Station")
  cityNetwork.addEdge("Starbucks", "MIT")
  cityNetwork.addEdge("Starbucks", "Harvard University")
  cityNetwork.addEdge("Harvard Square", "Grand Library of All Books")
  cityNetwork.addEdge("Harvard Museum of Natural History & Arts", "Grand Library of All Books")
  cityNetwork.addEdge("Harvard Museum of Natural History & Arts", "Harvard University")
  cityNetwork.addEdge("Harvard Square", "Harvard University")
  
  cityNetwork.display()
  print("\nBreadth first search:")
  cityNetwork.bfs("Grand Library of All Books")
  print("\nDepth first search:")
  cityNetwork.dfs("Grand Library of All Books")

  
  start = "Grand Library of All Books"
  end = "Grocery Store"
  print(f"\nShortest route from {start} to {end}: {cityNetwork.route(start,end)}") # Print out the route (sequence of landmarks) of the shortest path.

  cityNetwork.addVertex("testing")
  print(f"\nShortest route from {"testing"} to {end}: {cityNetwork.route("testing",end)}")
  

if __name__ == "__main__":
    main()

# --------------------------------------------------------------------------

# Analysis Portion (Report)
'''
Document detailing your implementation, test cases, results, and your analysis of BFS vs. DFS in this application
Write a brief analysis of the differences between BFS and DFS in the context of your transportation network. Discuss the scenarios in which one might be preferred over the other-
'''
# ==========================================================================
'''
  After observing the works between BFS and DFS, we are able to indicate that BFS and DFS have distinct differences. To begin, in the context of our transportation network, BFS is useful 
  e

  The difference between Breadth-First Search (BFS) and Depth-First Search (DFS) is that BFS visits all of its neighbors from a star vertex before it visits all unvisited neighbors based 
  on the distance from the starting point compared to DFS where we go as deep into a graph as possible and backtrack if a deadend is hit. 

  The time complexities of BFS and DFS is O(V + E), where V is the number of vertices and E is the number of edges but may depend on the graph's structure. DFS is more space efficient 
  than BFS since it doesn't need to store all the vertices of a level.

  In the context of this project, we have implemented a graph and dijkstra's method based on and adjusted from the classes' lectures. The BFS method is implemented using a queue while  
  the DFS method uses a stack. The test cases include creating vertices and edges to test if the shortest path is given and if the searching methods work. The results of the test cases is that the program works. We 
  even tested for errors such as raising a value error when an edge is implemented incorrectly. For instance, if we mispell a vertex that has not been established and we try mapping it 
  as a road, an error will occur. 

  The scenarios in which we would prefer BFS over DFS is...




'''

# Documentation Output Portion 
# ==========================================================================
'''
Please refer to the documentation file to see output screenshots
'''

# ----------------------------------------------------------------------------
