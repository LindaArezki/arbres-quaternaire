
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from src import QuadTree, TkQuadTree

def test_sample():
    filename = "quadtree.txt"
    quadtree = QuadTree.from_file(filename)
    assert quadtree.depth == 4

def test_single():
    filename = "quadtree_easy.txt"
    quadtree = QuadTree.from_file(filename)
    assert quadtree.depth == 1
