import sys
import math
import operator

# go find the two vertices which have the lightest weight edge between them, while being in different clusters
# exactly the same logic
# start with the vertices all in their own clusters
# every stage put vertices together, into their own clusters, never connect two vertices in the same cluster

class Point:
   def __init__(self, x_coord , y_coord, weight):
      self.x = x_coord
      self.y = y_coord
      self.weight = weight
      self.coords = "(" + str(x_coord) + ", " + str(y_coord) + ", " + str(weight) + ")"
      self.list = []
   def __str__(self):
      return self.coords
   __repr__ = __str__
   def __lt__(self, obj):
      if self.x < obj.x:
         return 

def sortX(p1):
   return p1.x

def sortY(p1):
   return p1.y

def sortListX(list):
   return list[0].x


def makeCluster(clusters, p1, p2, chosen_edges):
   indice1 = searchCluster(clusters, p1)
   indice2 = searchCluster(clusters, p2)
   # print("indice1: " + str(indice1) + "indice2: " + str(indice2))
   if indice1 == indice2:
      # case where both points are in the same cluster already
      pass

   # need to delete old clusters from Clusters[]
   elif len(clusters[indice1]) == 1 and len(clusters[indice2]) == 1:
      chosen_edges.append([p1, p2])
      # case where both clusters hold one point, thus a new larger one
      joinClusters(clusters, indice1, indice2)
   
   elif len(clusters[indice1]) > 1 and len(clusters[indice2]) > 1:
      # case where both clusters hold multiple points, and we join them
      chosen_edges.append([p1, p2])
      joinClusters(clusters, indice1, indice2)
   
   elif len(clusters[indice1]) > 1 and len(clusters[indice2]) == 1:
      chosen_edges.append([p1, p2])
      joinClusters(clusters, indice1, indice2)

   elif len(clusters[indice1]) == 1 and len(clusters[indice2]) > 1:
      chosen_edges.append([p1, p2])
      joinClusters(clusters, indice1, indice2)

def joinClusters(clusters, indice1, indice2):
   list1 = clusters[indice1]
   list2 = clusters[indice2]
   list1.extend(list2)
   if(indice1 > indice2):
      del clusters[indice1]
      del clusters[indice2]
   if(indice1 < indice2):
      del clusters[indice2]
      del clusters[indice1]
   clusters.append(list1)

def newCluster(clusters, p1, p2):
   clusters.append([p1, p2])

def searchCluster(clusters, pointSearch):
   i = 0
   for cluster in clusters:
      for point in cluster:
         if(pointSearch == point):
            return i
      i += 1

def dfs(visited, order_visited, graph, node):
    if node not in visited:
        visited.add(node)
        order_visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, order_visited, graph, neighbor)


def main():
   # points only holds Point objects
   edges, vertices = read_file(sys.argv[1])
   sorted_edges = sorted(edges, key=operator.attrgetter("weight"))
   clusters = []

   for vertice in vertices:
      clusters.append([vertice])

   i = 0
   num_vertices = len(vertices)

   distances = []
   for edge in sorted_edges:
      distances.append([edge.x, edge.y, edge.weight])
   
   chosen_edges = []
   while len(chosen_edges) < num_vertices - 1:
      makeCluster(clusters, sorted_edges[i].x, sorted_edges[i].y, chosen_edges)
      i += 1

   # print("clusters: " + str(clusters))
   chosen_vertices = []
   for edge in chosen_edges:
      if edge[0] not in chosen_vertices:
         chosen_vertices.append(edge[0])
      if edge[1] not in chosen_vertices:
         chosen_vertices.append(edge[1])

   # print("chosen_edges: " + str(chosen_edges))
   # print("chosen_vertices: " + str(chosen_vertices))
   adjacency_list = {}
   alist = []
   for vertex in chosen_vertices:
      add_node(vertex, alist)
      adjacency_list[vertex] = []
   for edge in chosen_edges:
      add_edge(edge[0], edge[1], alist, adjacency_list)

   # print(adjacency_list)
   visited = set() # Set to keep track of visited nodes.
   order_visited = []
   dfs(visited, order_visited, adjacency_list, 0)
   if order_visited[0] != order_visited[-1]:
      order_visited.append(order_visited[0])

   # print(order_visited)
   total_weight = get_weight(order_visited, sorted_edges)
   finisher(order_visited, total_weight)

def finisher(hamiltonian_cycle, total_weight):
   print("Hamiltonian cycle of weight " + str(total_weight) + ":")
   final_vertice = len(hamiltonian_cycle)
   i = 1
   for vertex in hamiltonian_cycle:
      if (final_vertice == i):
         print(str(vertex), end='')
      else:
         print(str(vertex) + ", ", end='')
      i += 1
   print()


def get_weight(hamiltonian_cycle, sorted_edges):
   total = 0
   i = 0
   while i < len(hamiltonian_cycle) - 1:
      weight = get_edge_weight(hamiltonian_cycle[i], hamiltonian_cycle[i+1], sorted_edges)
      total += weight
      i += 1
   return total

def get_edge_weight(v1, v2, sorted_edges):
   for edge in sorted_edges:
      if(v1 == edge.x and v2 == edge.y):
         return edge.weight
      elif(v2 == edge.x and v1 == edge.y):
         return edge.weight

def add_node(node, alist):
  if node not in alist:
   alist.append(node)
 
def add_edge(node1, node2, alist, adjacency_list):
  if node1 in alist and node2 in alist:
     first = adjacency_list[node1]
     second = adjacency_list[node2]
     first.append(node2)
     second.append(node1)
     first = sorted(first)
     second = sorted(second)
     adjacency_list[node1] = first
     adjacency_list[node2] = second


def read_file(file_name):
   f = open(file_name, 'r')
   points_list = []
   line_list = f.readlines()
   num_edges = 0
   for line in line_list:
      line = line.replace(" ", '')
      line = line.replace("\n", '')
      splitted = line.split(",")
      points_list.append(Point(int(splitted[0]), int(splitted[1]), int(splitted[2])))
      num_edges +=1
   vertices = []
   for point in points_list:
      if(point.x) not in vertices:
         vertices.append(point.x)
      if(point.y) not in vertices:
         vertices.append(point.y)
   vertices = sorted(vertices)
   return points_list, vertices

main()

