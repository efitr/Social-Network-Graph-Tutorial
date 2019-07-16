
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
        

if __name__ == '__main__':
    unittest.main()
