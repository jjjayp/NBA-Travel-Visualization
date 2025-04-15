import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        # Create a simple test graph.
        self.g = Graph(V=("A", "B", "C", "D", "E"),
                       E=[("A", "B", 100),
                          ("B", "C", 200),
                          ("A", "D", 300),
                          ("D", "E", 400),
                          ("C", "E", 150)])
    
    def test_add_vertex(self):
        self.g.add_vertex("F")
        self.assertIn("F", self.g.vertices)

    def test_remove_vertex(self):
        self.g.remove_vertex("A")
        self.assertNotIn("A", self.g.vertices)

    def test_add_edge(self):
        self.g.add_edge("A", "F", 123)
        self.assertIn("F", self.g.edges["A"])

    def test_remove_edge(self):
        self.g.remove_edge("A", "B", 100)
        self.assertNotIn("B", self.g.edges["A"])

    def test_fewest_flights(self):
        # Ensure BFS returns a valid predecessor map.
        pred = self.g.fewest_flights("A")
        self.assertEqual(pred["A"], None)
        self.assertIn("B", pred)

    def test_shortest_path(self):
        sp = self.g.shortest_path("A")
        self.assertEqual(sp["A"], (None, 0))
        # Check that distance to E is computed.
        self.assertTrue(sp["E"][1] < float('inf'))

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)

