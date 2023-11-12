
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from src import QuadTree, TkQuadTree

# Verifie la profondeur du quadtree d'un fichier récupéré
def test_sample():
    filename = "quadtree.txt"
    quadtree = QuadTree.from_file(filename)
    assert quadtree.depth == 4

def test_single():
    filename = "quadtree_easy.txt"
    quadtree = QuadTree.from_file(filename)
    assert quadtree.depth == 1

# Verifie les élements récuperés par un fichier donnée
def test_elements_quadtree():
    filename = "quadtree.txt"
    quadtree = QuadTree.from_file(filename)
    assert str(quadtree) == "[[0, 0, 0, [1, 0, 0, 0]], [0, 0, [0, 1, 0, 0], 0], [0, 0, 0, [[1, 0, 0, 1], [0, 0, 1, 1], 0, 0]], [0, 0, [[0, 0, 1, 1], [0, 1, 1, 0], 0, 0], 0]]"

def test_elements_quadtree_easy():
    filename = "quadtree_easy.txt"
    quadtree = QuadTree.from_file(filename)
    assert str(quadtree) == "[0, 1, 0, 1]"
