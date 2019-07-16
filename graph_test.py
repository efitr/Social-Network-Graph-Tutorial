
from graph import Graph, Vertex
import random
import unittest

class TestVertex(unittest.TestCase):
    def test__init__(self):
        vertex = Vertex('Egon')
        assert vertex.id == 'Egon'
        assert vertex.neighbors == {}
        # assert vertex.get_neighbors() == {}

    def test_add_neighbor(self):
        egon_vertex = Vertex('Egon')
        yurac_vertex = Vertex('Yurac') 
        # Make to check the main values in both Vertex
        print("Egon Vertex: ", egon_vertex.id)
        print(egon_vertex.add_neighbor(yurac_vertex))
        assert egon_vertex.add_neighbor(yurac_vertex)
        assert egon_vertex.neighbors == {yurac_vertex: 'yurac_vertex'}

    # def test_more_complex_add_neighbor(self):


if __name__ == '__main__':
    unittest.main()
