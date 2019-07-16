#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

# class Node(object):
class Vertex(object):
# class Point(object): # Worst one on my opinion

    def __init__(self, vertex):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        # 
        self.node_name = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        # TODO check if vertex is already a neighbor
        # This should 
        self.neighbors[vertex] = vertex.node_name


        # TODO if not, add vertex to neighbors and assign weight.

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.node_name} adjacent to {[x.node_name for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        # TODO return the neighbors
        return self.neighbors

    def get_node_name(self):
        """Return the node_name of this vertex."""
        return self.node_name

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # TODO return the weight of the edge from this
        # vertex to the given vertex.


""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""
''' Remember
Think of a Graph as a a Network 
'''


# class Network:
class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary."""
        self.network_elements = {}
        self.numVertices = 0

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        # TODO increment the number of vertices
        self.numVertices += 1
        # TODO create a new vertex
        new_vertex = Vertex('Egon')
        # TODO add the new vertex to the vertex list
        new_vertex_node_name = new_vertex.node_name
        # TODO return the new vertex
        print()

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        # TODO return the vertex if it is in the graph

    def add_edge(self, key1, key2, weight=0):
        """add an edge from vertex with key `key1` to vertex with key `key2` with a weight."""
        # TODO if either vertex is not in the graph,
        # add it - or return an error (choice is up to you).
        # TODO if both vertices in the graph, add the
        # edge by making key1 a neighbor of key2
        # and using the addNeighbor method of the Vertex class.
        # Hint: the vertex key1 is stored in self.vertList[f].

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.network_elements.keys()

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.network_elements.values())


# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print("( %s , %s )" % (v.getnode_name(), w.getnode_name()))
